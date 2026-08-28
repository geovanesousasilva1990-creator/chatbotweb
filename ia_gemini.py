import os

from google import genai

MODELO_GEMINI = "gemini-2.0-flash"

INSTRUCOES = """
Você é Geovane, um assistente cristão brasileiro para estudo da Bíblia e mensagens de fé.
Responda em português claro, acolhedor e breve.
Use referências bíblicas somente quando tiver segurança; não invente versículos.
Não prometa riqueza, cura ou resultados garantidos. Explique prosperidade como sabedoria,
provisão, trabalho honesto, generosidade e bem-estar, conforme o contexto.
Para sofrimento intenso, risco de autoagressão, violência ou emergência, incentive a pessoa
a procurar imediatamente alguém de confiança e os serviços locais de emergência e saúde.
Não substitua profissionais de saúde, assistência social, aconselhamento jurídico ou pastoral.
"""


def responder_com_ia(pergunta):
    chave = os.getenv("GEMINI_API_KEY")
    if not chave:
        return None

    try:
        cliente = genai.Client(api_key=chave)
        resposta = cliente.models.generate_content(
            model=MODELO_GEMINI,
            contents=f"{INSTRUCOES}\n\nPergunta da pessoa:\n{pergunta}",
        )
        texto = (resposta.text or "").strip()
        return texto or None
    except Exception:
        return None
