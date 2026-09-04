import os
import re
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
Se a pessoa enviar apenas uma palavra bíblica, explique seu significado na Bíblia, indique uma referência segura e pergunte se ela deseja aprofundar.
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

RESPOSTAS_TERMOS_BIBLICOS = {
    "arca": "Na Bíblia, a arca de Noé representa o livramento de Deus em meio ao juízo. Leia Gênesis 6–9. Também existe a arca da aliança, ligada à presença de Deus entre Israel.",
    "alianca": "Aliança é um compromisso estabelecido por Deus com seu povo. A Bíblia apresenta alianças com Noé, Abraão, Israel e a nova aliança em Cristo. Leia Jeremias 31:31-34.",
    "altar": "O altar era um lugar de culto, entrega e busca de Deus. Na vida cristã, ele lembra uma fé sincera e uma vida oferecida ao Senhor. Leia Romanos 12:1.",
    "anjo": "Anjos são mensageiros e servos de Deus na narrativa bíblica. A Bíblia orienta que a adoração pertence somente a Deus. Leia Hebreus 1:14.",
    "batismo": "O batismo é um sinal público de fé e compromisso com Cristo, associado à nova vida. Igrejas cristãs podem praticá-lo de formas diferentes. Leia Romanos 6:3-4.",
    "cruz": "A cruz é o centro da mensagem cristã: nela Jesus entregou sua vida e, segundo a fé cristã, venceu o pecado e a morte. Leia 1 Coríntios 1:18.",
    "jejum": "O jejum bíblico é uma prática de oração, humildade e busca de Deus, não uma maneira de obrigá-lo a agir. Faça-o com responsabilidade e cuide da saúde. Leia Mateus 6:16-18.",
    "parabola": "Parábolas são histórias usadas por Jesus para ensinar verdades sobre o Reino de Deus e a vida com Deus. Leia Mateus 13:34-35.",
    "profeta": "Profeta era alguém chamado para transmitir a mensagem de Deus, denunciar injustiças e anunciar esperança. Leia Miquéias 6:8.",
    "templo": "O templo era um lugar central de adoração em Israel. No Novo Testamento, a comunidade e a vida do cristão também são descritas como lugar da presença do Espírito. Leia 1 Coríntios 6:19.",
    "ressurreicao": "Ressurreição é a vitória sobre a morte. Para a fé cristã, a ressurreição de Jesus é o fundamento da esperança. Leia 1 Coríntios 15:3-4.",
    "santidade": "Santidade significa pertencer a Deus e buscar uma vida transformada, com amor, justiça e integridade. Leia 1 Pedro 1:15-16.",
    "reino": "O Reino de Deus aponta para o governo e a vontade de Deus. Jesus ensinou que ele deve orientar a vida, a justiça e o amor ao próximo. Leia Mateus 6:33.",
    "sacerdote": "O sacerdote exercia funções de culto e serviço no antigo Israel. A carta aos Hebreus apresenta Jesus como sumo sacerdote na nova aliança. Leia Hebreus 4:14-16.",
    "milagre": "Milagre é um acontecimento extraordinário atribuído à ação de Deus. Nos Evangelhos, os milagres de Jesus expressam poder e compaixão. Leia Marcos 1:40-42.",
}

TERMOS_DO_ESCOPO = {
    "biblia", "bíblia", "biblico", "bíblico", "versiculo", "versículo", "deus", "jesus", "cristo",
    "evangelho", "igreja", "oracao", "oração", "fe", "fé", "espirito santo",
    "salvacao", "salvação", "pecado", "perdao", "perdão", "graca", "graça",
    "devocional", "salmo", "salmos", "proverbio", "provérbio", "apóstolo",
    "apostolo", "pastor", "louvor", "adoracao", "adoração", "bencao", "bênção",
    "motivacao", "motivação", "esperanca", "esperança", "coragem", "ansioso",
        "apostolo", "apóstolo", "apostolos", "apóstolos", "discipulo", "discípulo",
        "discipulos", "discípulos", "devocional", "devocionais",
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
    "arca", "aliança", "alianca", "altar", "anjo", "apocalipse", "arca de noé",
    "bênção", "bencao", "cativeiro", "circuncisão", "circuncisao", "concerto",
    "cruz", "discípulo", "discipulo", "dízimo", "dizimo", "êxodo", "exodo",
    "genealogia", "glória", "gloria", "holocausto", "idolatria", "jejum",
    "jerusalém", "jerusalem", "judaísmo", "judaismo", "lei", "maná", "mana",
    "messias", "milagre", "milagres", "ministério", "ministerio", "nazareno",
    "pacto", "parábola", "parabola", "pentecostes", "profecia", "profecia",
    "profeta", "redenção", "redencao", "reino", "ressurreição", "ressurreicao",
    "sacerdote", "sacrifício", "sacrificio", "santidade", "sermão", "sermao",
    "tabernáculo", "tabernaculo", "templo", "testamento", "trindade", "ungido",
    "visão", "visao", "vontade", "adoração", "adoracao", "arrependimento",
    "batismo", "consolo", "consolo", "criação", "criacao", "discernimento",
}


def pergunta_no_escopo(pergunta):
    texto = unicodedata.normalize("NFKD", pergunta.lower())
    texto = "".join(
        caractere for caractere in texto
        if not unicodedata.combining(caractere)
    )
    return any(
        re.search(rf"(?<!\w){re.escape(termo)}(?!\w)", texto)
        for termo in TERMOS_DO_ESCOPO
    )


def resposta_termo_biblico(pergunta):
    texto = unicodedata.normalize("NFKD", pergunta.lower())
    texto = "".join(caractere for caractere in texto if not unicodedata.combining(caractere))
    palavras = re.findall(r"[a-z]+", texto)
    for palavra in palavras:
        if palavra in RESPOSTAS_TERMOS_BIBLICOS:
            return RESPOSTAS_TERMOS_BIBLICOS[palavra]
    return None


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
