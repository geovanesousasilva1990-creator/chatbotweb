import os
import unicodedata

from google import genai

MODELO_GEMINI = "gemini-2.0-flash"

INSTRUCOES = """
Você é Geovane, um assistente cristão brasileiro para estudo da Bíblia e mensagens de fé.
Responda somente sobre Bíblia, fé cristã, oração, vida espiritual, devocionais e motivação
com base em valores cristãos. Para qualquer outro assunto, responda apenas: "Posso ajudar
somente com perguntas sobre Bíblia, fé e motivação cristã."
Responda em português claro, acolhedor e breve, mas desenvolva a explicação em 2 ou 3 parágrafos quando a pergunta pedir estudo.
Quando fizer sentido, organize a resposta em: contexto bíblico, ensinamento principal e aplicação prática.
Não trate uma interpretação de uma denominação como consenso: sinalize brevemente quando houver diferenças entre tradições cristãs.
Use referências bíblicas somente quando tiver segurança; não invente versículos.
Não prometa riqueza, cura ou resultados garantidos. Explique prosperidade como sabedoria,
provisão, trabalho honesto, generosidade e bem-estar, conforme o contexto.
Para sofrimento intenso, risco de autoagressão, violência ou emergência, incentive a pessoa
a procurar imediatamente alguém de confiança e os serviços locais de emergência e saúde.
Não substitua profissionais de saúde, assistência social, aconselhamento jurídico ou pastoral.
"""

RESPOSTA_FORA_DO_ESCOPO = (
    "Posso ajudar somente com perguntas sobre Bíblia, fé e motivação cristã."
)

TERMOS_DO_ESCOPO = {
    "biblia", "bíblia", "versiculo", "versículo", "deus", "jesus", "cristo",
    "evangelho", "igreja", "oracao", "oração", "fe", "fé", "espirito santo",
    "salvacao", "salvação", "pecado", "perdao", "perdão", "graca", "graça",
    "devocional", "salmo", "salmos", "proverbio", "provérbio", "apóstolo",
    "apostolo", "pastor", "louvor", "adoracao", "adoração", "bencao", "bênção",
    "motivacao", "motivação", "esperanca", "esperança", "coragem", "ansioso",
    "ansiedade", "triste", "tristeza", "desanimado", "desanimo", "desânimo",
    "sofrimento", "superar", "propósito", "proposito", "vida",
    "genesis", "gênesis", "exodo", "êxodo", "levitico", "levítico", "numeros",
    "números", "deuteronomio", "deuteronômio", "josue", "josué", "juizes", "juízes",
    "rute", "samuel", "reis", "cronicas", "crônicas", "esdras", "neemias", "ester",
    "jo", "jó", "eclesiastes", "canticos", "cânticos", "isaias", "isaías",
    "jeremias", "lamentacoes", "lamentações", "ezequiel", "daniel", "oseias", "oséias",
    "joel", "amos", "amós", "obadias", "jonas", "miqueias", "miquéias", "naum", "naum",
    "habacuque", "sofonias", "ageu", "zacarias", "malaquias", "mateus", "marcos", "lucas",
    "joao", "joão", "atos", "romanos", "corintios", "coríntios", "galatas", "gálatas",
    "efesios", "efésios", "filipenses", "colossenses", "tessalonicenses", "timoteo",
    "timóteo", "tito", "filemom", "hebreus", "tiago", "pedro", "joao", "joão", "judas",
    "apocalipse", "revelacao", "revelação",
}


def pergunta_no_escopo(pergunta):
    texto = unicodedata.normalize("NFKD", pergunta.lower())
    texto = "".join(
        caractere for caractere in texto
        if not unicodedata.combining(caractere)
    )
    return any(termo in texto for termo in TERMOS_DO_ESCOPO)


def responder_com_ia(pergunta):
    if not pergunta_no_escopo(pergunta):
        return RESPOSTA_FORA_DO_ESCOPO

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
