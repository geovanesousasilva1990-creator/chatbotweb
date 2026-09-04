import unicodedata

from flask import Flask, render_template, request, jsonify
from chatbot import RESPOSTA_PADRAO, responder, buscar_versiculo
from ia_gemini import responder_com_ia
from modelo_ml import listar_biblioteca, listar_devocionais, registrar_aprendizado, LIVRO_SLUGS, RESPOSTAS_ML
from database import registrar_resposta

app = Flask(__name__)


def _normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def _resposta_livro_biblia(mensagem):
    texto = _normalizar_texto(mensagem)

    if "livros da biblia" in texto or "livros da bíblia" in texto:
        return RESPOSTAS_ML.get("livros_biblia")

    for livro, slug in LIVRO_SLUGS.items():
        livro_normalizado = _normalizar_texto(livro)
        if livro_normalizado in texto or slug in texto:
            return RESPOSTAS_ML.get(slug)

    return None

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/devocionais")
def devocionais():
    return jsonify({"devocionais": listar_biblioteca()})


@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json(silent=True)
    mensagem = dados.get("mensagem", "").strip() if isinstance(dados, dict) else ""
    if not mensagem:
        return jsonify({"erro": "Digite uma pergunta para continuar."}), 400

    # Tentar responder primeiro no servidor com os livros da Bíblia
    resposta_livro = _resposta_livro_biblia(mensagem)

    # Tentar buscar versículo na API (ex: "João 3:16")
    resultado_versiculo = buscar_versiculo(mensagem)

    resposta_local = responder(mensagem)

    if resposta_livro:
        resposta = resposta_livro
    elif resultado_versiculo:
        resposta = resultado_versiculo
    elif resposta_local != RESPOSTA_PADRAO:
        resposta = resposta_local
    else:
        resposta = responder_com_ia(mensagem) or resposta_local

    registrar_resposta(mensagem, resposta, categoria="biblia", fonte="chatbot")
    return jsonify({"resposta": resposta})


@app.route("/feedback", methods=["POST"])
def feedback():
    dados = request.get_json(silent=True)
    pergunta = dados.get("pergunta", "").strip().lower() if isinstance(dados, dict) else ""
    if not pergunta:
        return jsonify({"ok": False}), 400

    aprendeu = registrar_aprendizado(pergunta)
    return jsonify({"ok": aprendeu})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)