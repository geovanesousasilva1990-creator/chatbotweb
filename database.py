import json
import os
import sqlite3
from pathlib import Path

try:
    import psycopg2
except Exception:
    psycopg2 = None

JSON_DB_PATH = Path(__file__).with_name("banco_respostas_biblicas.json")
SQLITE_DB_PATH = Path(__file__).with_name("respostas_biblicas.db")


def _db_url():
    return os.getenv("DATABASE_URL")


def _connect_sqlite():
    conn = sqlite3.connect(SQLITE_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def _connect_postgres():
    if not psycopg2:
        raise RuntimeError("psycopg2 não instalado. Instale com pip install psycopg2-binary")

    url = _db_url()
    if not url:
        raise RuntimeError("DATABASE_URL não configurada")

    return psycopg2.connect(url)


def _connect_db():
    url = _db_url()
    if url:
        return _connect_postgres()
    return _connect_sqlite()


def _ensure_schema():
    conn = _connect_db()
    try:
        if _db_url():
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS respostas_biblicas (
                        id SERIAL PRIMARY KEY,
                        pergunta TEXT NOT NULL,
                        resposta TEXT NOT NULL,
                        categoria TEXT DEFAULT 'biblia',
                        fonte TEXT DEFAULT 'chatbot',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """
                )
                conn.commit()
        else:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS respostas_biblicas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pergunta TEXT NOT NULL,
                    resposta TEXT NOT NULL,
                    categoria TEXT DEFAULT 'biblia',
                    fonte TEXT DEFAULT 'chatbot',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()
    finally:
        conn.close()


def _carregar_db():
    if _db_url():
        conn = _connect_db()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT pergunta, resposta, categoria, fonte FROM respostas_biblicas ORDER BY id ASC"
                )
                return [
                    {
                        "pergunta": row[0],
                        "resposta": row[1],
                        "categoria": row[2],
                        "fonte": row[3],
                    }
                    for row in cur.fetchall()
                ]
        finally:
            conn.close()

    if not JSON_DB_PATH.exists():
        return []

    try:
        with JSON_DB_PATH.open("r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _salvar_db(registros):
    if _db_url():
        conn = _connect_db()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM respostas_biblicas")
                for item in registros:
                    cur.execute(
                        "INSERT INTO respostas_biblicas (pergunta, resposta, categoria, fonte) VALUES (%s, %s, %s, %s)",
                        (item.get("pergunta", ""), item.get("resposta", ""), item.get("categoria", "biblia"), item.get("fonte", "chatbot")),
                    )
            conn.commit()
        finally:
            conn.close()
        return

    with JSON_DB_PATH.open("w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, ensure_ascii=False, indent=2)


def registrar_resposta(pergunta, resposta, categoria="biblia", fonte="chatbot"):
    _ensure_schema()
    item = {
        "pergunta": pergunta.strip(),
        "resposta": resposta.strip(),
        "categoria": categoria,
        "fonte": fonte,
    }

    if not item["pergunta"] or not item["resposta"]:
        return False

    if _db_url():
        conn = _connect_db()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT 1 FROM respostas_biblicas WHERE pergunta = %s AND resposta = %s LIMIT 1",
                    (item["pergunta"], item["resposta"]),
                )
                if cur.fetchone():
                    return True
                cur.execute(
                    "INSERT INTO respostas_biblicas (pergunta, resposta, categoria, fonte) VALUES (%s, %s, %s, %s)",
                    (item["pergunta"], item["resposta"], item["categoria"], item["fonte"]),
                )
            conn.commit()
            return True
        finally:
            conn.close()

    registros = _carregar_db()
    if any(r.get("pergunta", "").strip() == item["pergunta"] and r.get("resposta", "").strip() == item["resposta"] for r in registros):
        return True

    registros.append(item)
    _salvar_db(registros)
    return True


def listar_respostas(limit=50):
    registros = _carregar_db()
    return registros[-limit:] if limit else registros


def limpar_respostas():
    if _db_url():
        conn = _connect_db()
        try:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM respostas_biblicas")
            conn.commit()
        finally:
            conn.close()
        return True

    _salvar_db([])
    return True
