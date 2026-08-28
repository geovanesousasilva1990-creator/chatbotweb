import json
import unicodedata
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

ARQUIVO_APRENDIZADO = Path(__file__).with_name("dados_aprendizado.json")

EXEMPLOS = [
    ("oi olá bom dia boa tarde opa", "saudacao"),
    ("qual seu nome quem é você", "nome"),
    ("quem é Jesus filho de Deus salvador", "jesus"),
    ("como alcançar salvação vida eterna", "salvacao"),
    ("o que é fé acreditar em Deus", "fe"),
    ("o que é graça misericórdia de Deus", "graca"),
    ("como pedir perdão pecado arrependimento", "perdao"),
    ("como fazer oração orar Pai Nosso", "oracao"),
    ("o que é amor mandamento amar próximo", "amor"),
    ("fale sobre Moisés Êxodo", "moises"),
    ("fale sobre Davi Salmos Golias", "davi"),
    ("quem foi Maria mãe de Jesus", "maria"),
    ("quem foram os apóstolos discípulos", "apostolos"),
    ("quais são os livros da Bíblia", "livros_biblia"),
    ("o que é Antigo Testamento", "antigo_testamento"),
    ("o que é Novo Testamento Evangelhos", "novo_testamento"),
    ("Jesus fez milagres cura tempestade", "milagres"),
    ("o que é céu paraíso", "ceu"),
    ("estou triste preciso de esperança mensagem de fé", "esperanca"),
    ("sem forças abatido cansado desanimado palavra de esperança", "esperanca"),
    ("estou ansioso preocupado com medo preciso de Deus", "ansiedade"),
    ("mente preocupada pensamentos ansiedade medo", "ansiedade"),
    ("estou passando por dificuldade prova luta mensagem de força", "coragem"),
    ("preciso continuar seguir em frente palavra de força", "coragem"),
    ("perdi alguém estou de luto preciso de consolo", "consolo"),
    ("quero agradecer a Deus gratidão bênçãos", "gratidao"),
    ("preciso confiar em Deus mensagem para hoje", "confianca"),
    ("mensagem de esperança futuro melhor dias bons", "esperanca_biblica"),
    ("acreditar que o futuro vai melhorar esperança dias melhores", "esperanca_biblica"),
    ("quero prosperidade bênção provisão trabalho sucesso financeiro", "prosperidade"),
    ("organizar minha vida financeira com Deus prosperidade provisão", "prosperidade"),
    ("preciso ser fortalecido Deus estou fraco não desista", "fortalecimento"),
    ("como ter uma vida próspera com sabedoria bíblica", "prosperidade"),
    ("dê força para enfrentar problemas e continuar", "fortalecimento"),
    ("mensagem de autoajuda motivação para hoje", "autoajuda"),
    ("preciso melhorar minha vida e ter disciplina", "disciplina"),
    ("baixa autoestima não acredito em mim", "autoestima"),
    ("como recomeçar depois de errar", "recomeco"),
    ("indique livros da bíblia para me ajudar", "livros_ajuda"),
    ("quais livros de autoajuda posso ler", "livros_autoajuda"),
    ("livros para esperança fé amor e respeito", "livros_autoajuda"),
    ("como alcançar intimidade com Deus", "intimidade_deus"),
    ("como me aproximar mais de Deus", "intimidade_deus"),
    ("como viver com amor e respeito", "amor_respeito"),
    ("mensagem de amor respeito ao próximo", "amor_respeito"),
    ("como foi a criação do mundo quem criou o universo", "criacao"),
    ("o que é pecado como vencer o pecado", "pecado"),
    ("quem é o Espírito Santo o que ele faz", "espirito_santo"),
    ("o que é batismo por que ser batizado", "batismo"),
    ("como obter sabedoria segundo a Bíblia", "sabedoria"),
    ("indique livros devocionais para ler", "livros_devocionais"),
    ("quais livros de devocional você recomenda", "livros_devocionais"),
    ("quero começar um devocional diário", "livros_devocionais"),
    ("livros cristãos para fortalecer minha fé", "livros_devocionais"),
    ("O Salvador Chegou", "livros_devocionais"),
    ("Nome Sobre Todo Nome", "livros_devocionais"),
    ("Devocionais das Maravilhas", "livros_devocionais"),
    ("Você Está com Medo", "livros_devocionais"),
    ("99 Sermões para Vida com Deus", "livros_devocionais"),
    ("Devocionais Bíblicos Gratuitos fé propósito adoração", "livros_devocionais"),
    ("Devocional Diário 30 Dias com Deus oração", "livros_devocionais"),
    ("Guia Devocional de 21 Dias para Jejum e Oração Isaías", "livros_devocionais"),
    ("Devocional A Forja Crescimento Espiritual", "livros_devocionais"),
    ("Devocional de 21 Dias para Negócios trabalho finanças", "livros_devocionais"),
    ("quais são os livros devocionais cadastrados", "livros_devocionais"),
    ("quero um desafio de fé", "desafios_fe"),
    ("desafio cristão para hoje", "desafios_fe"),
    ("proponha um desafio espiritual", "desafios_fe"),
    ("como praticar minha fé durante a semana", "desafios_fe"),
]

RESPOSTAS_ML = {
    "saudacao": "Olá! Sou Geovane, um chatbot especializado em Bíblia. O que você gostaria de estudar?",
    "nome": "Meu nome é Geovane, um chatbot criado para ajudar no estudo da Bíblia.",
    "jesus": "Jesus é o Filho de Deus e nosso Salvador. Ele ensinou o amor, morreu na cruz e ressuscitou ao terceiro dia.",
    "salvacao": "A Bíblia apresenta a salvação como vida eterna em Cristo. João 3:16 fala do amor de Deus e da fé em seu Filho.",
    "fe": "Fé é confiar em Deus e em suas promessas. Hebreus 11:1 ensina que a fé é a certeza do que se espera.",
    "graca": "Graça é o favor e a misericórdia de Deus, recebidos não por merecimento, mas por sua bondade.",
    "perdao": "A Bíblia ensina que Deus oferece perdão a quem se arrepende sinceramente e busca uma vida transformada.",
    "oracao": "Oração é conversar com Deus com sinceridade, apresentando pedidos, agradecimentos e preocupações.",
    "amor": "O amor é um dos maiores ensinamentos bíblicos. Jesus ensinou a amar a Deus e ao próximo.",
    "moises": "Moisés liderou Israel, recebeu os Dez Mandamentos e guiou o povo pelo deserto.",
    "davi": "Davi foi rei de Israel, venceu Golias e é associado a muitos dos Salmos.",
    "maria": "Maria foi a mãe de Jesus e aparece nos Evangelhos como serva de Deus.",
    "apostolos": "Jesus escolheu doze apóstolos para anunciar o Evangelho e testemunhar seus ensinamentos.",
    "livros_biblia": "A Bíblia tem 66 livros na tradição protestante, divididos entre Antigo e Novo Testamento. Pergunte pelos livros da Bíblia para ver a lista completa.",
    "antigo_testamento": "O Antigo Testamento reúne 39 livros na tradição protestante, desde Gênesis até Malaquias.",
    "novo_testamento": "O Novo Testamento reúne 27 livros, começando por Mateus e terminando em Apocalipse.",
    "milagres": "Os Evangelhos relatam que Jesus curou pessoas, acalmou tempestades, alimentou multidões e realizou outros milagres.",
    "ceu": "A Bíblia descreve o céu como a esperança da presença de Deus e da vida eterna para os que creem.",
    "esperanca": "Mesmo em dias difíceis, há esperança. 'O choro pode durar uma noite, mas a alegria vem pela manhã' (Salmos 30:5). Respire, ore e procure também alguém de confiança para caminhar com você.",
    "ansiedade": "Deus se importa com suas preocupações. Filipenses 4:6-7 ensina a apresentar os pedidos a Deus em oração. Se a ansiedade estiver intensa, procure também ajuda de um profissional de saúde.",
    "coragem": "Você não precisa enfrentar tudo sozinho. 'Sê forte e corajoso; não temas' (Josué 1:9). Dê um passo de cada vez e peça apoio a pessoas de confiança.",
    "consolo": "Sinto muito pela sua perda. A Bíblia diz que Deus está perto dos que têm o coração quebrantado (Salmos 34:18). Permita-se viver o luto e procure companhia e apoio.",
    "gratidao": "A gratidão reconhece as bênçãos, mesmo nas pequenas coisas. 'Este é o dia que o Senhor fez; alegremo-nos' (Salmos 118:24).",
    "confianca": "Confie seus caminhos a Deus com sinceridade. Provérbios 3:5-6 ensina a confiar no Senhor e buscar sua direção em cada passo.",
    "esperanca_biblica": "A esperança bíblica aponta para um futuro cuidado por Deus. 'Eu é que sei que pensamentos tenho a vosso respeito... pensamentos de paz e não de mal, para vos dar o fim que desejais' (Jeremias 29:11). Continue com fé e dê um passo de cada vez.",
    "prosperidade": "Na Bíblia, prosperidade não é uma promessa de riqueza fácil. Ela envolve sabedoria, trabalho honesto, contentamento e cuidado de Deus. 'O Senhor te abençoe e te guarde' (Números 6:24). Planeje com responsabilidade e pratique generosidade.",
    "fortalecimento": "Deus pode renovar suas forças. 'Os que esperam no Senhor renovarão as suas forças' (Isaías 40:31). Não enfrente tudo sozinho: ore, descanse e procure apoio de pessoas confiáveis.",
    "autoajuda": "Comece pequeno: escolha uma atitude boa para hoje, faça uma pausa para respirar e não se cobre resolver tudo de uma vez. 'Tudo posso naquele que me fortalece' (Filipenses 4:13).",
    "disciplina": "Disciplina é constância, não perfeição. Defina uma tarefa simples, cumpra-a hoje e repita amanhã. Provérbios 21:5 lembra que os planos diligentes conduzem à abundância.",
    "autoestima": "Seu valor não depende de erros, aparência ou opinião dos outros. Você é uma pessoa digna de cuidado e respeito. 'Eu te louvo porque me fizeste de modo especial' (Salmos 139:14).",
    "recomeco": "Errar não precisa ser o fim. Reconheça o que aconteceu, aprenda, peça perdão quando necessário e dê o próximo passo. 'As misericórdias do Senhor... renovam-se cada manhã' (Lamentações 3:22-23).",
    "livros_ajuda": "Para encontrar orientação e encorajamento, leia: Provérbios (sabedoria prática), Salmos (oração e consolo), Eclesiastes (propósito), Filipenses (alegria e perseverança), Tiago (fé em ação) e Romanos (esperança).",
    "livros_autoajuda": "Para uma jornada de crescimento, leia:\n\nBíblia: Provérbios (sabedoria), Salmos (oração e consolo), Eclesiastes (propósito), Filipenses (alegria e perseverança), Tiago (fé em ação), Romanos (esperança), João (vida de Jesus), Mateus (ensinamentos de Jesus) e 1 Coríntios (amor).\n\nDesenvolvimento pessoal: 'O Poder do Hábito', de Charles Duhigg (hábitos); 'Mindset', de Carol Dweck (mentalidade de crescimento); 'Hábitos Atômicos', de James Clear (pequenas mudanças); 'Essencialismo', de Greg McKeown (foco); e 'A Coragem de Ser Imperfeito', de Brené Brown (autenticidade). Leia com senso crítico e escolha o que combina com sua realidade.",
    "intimidade_deus": "A intimidade com Deus cresce com constância, não com pressa: reserve um momento diário para oração sincera, leia um trecho da Bíblia, pratique o que aprendeu, agradeça e sirva alguém com amor. Comece por João, Salmos e Tiago. 'Chegai-vos a Deus, e ele se chegará a vós' (Tiago 4:8).",
    "amor_respeito": "Amor e respeito aparecem em atitudes: escute sem humilhar, fale a verdade com gentileza, perdoe sem aceitar abusos e trate cada pessoa com dignidade. Leia 1 Coríntios 13, Romanos 12 e Efésios 4. Se houver violência, procure ajuda e um local seguro.",
    "criacao": "Gênesis 1 apresenta Deus como o Criador dos céus, da terra, da luz, dos animais e da humanidade. A criação também convida ao cuidado responsável com a vida e com o mundo.",
    "pecado": "Pecado é tudo o que se opõe à vontade de Deus e prejudica nosso relacionamento com Ele e com o próximo. A Bíblia ensina arrependimento, fé, perdão e uma mudança de vida com ajuda de Deus.",
    "espirito_santo": "O Espírito Santo é apresentado na Bíblia como a presença de Deus que consola, orienta e fortalece os que creem. Ele ajuda a viver a fé e a produzir atitudes de amor, alegria, paz e domínio próprio.",
    "batismo": "O batismo é um sinal público de fé e compromisso com Cristo. Ele representa uma nova vida e a união com Jesus. Igrejas cristãs podem praticá-lo de formas diferentes, por isso vale conversar com uma comunidade de confiança.",
    "sabedoria": "A Bíblia relaciona sabedoria ao temor do Senhor, à humildade e à prática do bem. Leia Provérbios e Tiago 1:5; peça direção a Deus e também ouça conselhos responsáveis.",
    "livros_devocionais": "Os devocionais cadastrados são:\n\n- 'O Salvador Chegou'\n- 'Nome Sobre Todo Nome'\n- 'Devocionais das Maravilhas'\n- 'Você Está com Medo'\n- '99 Sermões para Vida com Deus'\n- 'Devocionais Bíblicos Gratuitos': 75 devocionais curtos sobre fé, propósito e adoração\n- 'Devocional Diário: 30 Dias com Deus': rotina de oração diária\n- 'Guia Devocional de 21 Dias para Jejum e Oração': baseado em Isaías\n- 'Devocional A Forja: Crescimento Espiritual': amadurecimento na fé cristã\n- 'Devocional de 21 Dias para Negócios': princípios bíblicos para trabalho e finanças\n\nPosso ajudar você a escolher um para começar. Leia um trecho por dia, anote o que aprendeu e termine com uma oração.",
    "desafios_fe": "Desafio de fé para hoje: reserve 10 minutos para oração, leia Filipenses 4, anote três motivos de gratidão e envie uma mensagem de encorajamento a alguém. Durante a semana, pratique um ato de serviço, perdoe uma ofensa possível e separe um momento sem distrações para refletir. Faça tudo com liberdade e sinceridade, sem transformar a fé em cobrança.",
}

def normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


_vetorizador = TfidfVectorizer(
    preprocessor=normalizar_texto,
    lowercase=False,
    ngram_range=(1, 2),
)
_modelo = NearestNeighbors(n_neighbors=1, metric="cosine")
_rotulos_treinamento = []


def _treinar():
    exemplos = list(EXEMPLOS)
    if ARQUIVO_APRENDIZADO.exists():
        try:
            aprendidos = json.loads(ARQUIVO_APRENDIZADO.read_text(encoding="utf-8"))
            exemplos.extend((item["pergunta"], item["rotulo"]) for item in aprendidos)
        except (OSError, ValueError, KeyError, TypeError):
            pass

    textos, rotulos = zip(*exemplos)
    global _rotulos_treinamento
    _rotulos_treinamento = list(rotulos)
    _modelo.fit(_vetorizador.fit_transform(textos))


_treinar()


def classificar_intencao(pergunta):
    vetor = _vetorizador.transform([normalizar_texto(pergunta)])
    if vetor.nnz == 0:
        return None, 0.0
    distancia, _ = _modelo.kneighbors(vetor, n_neighbors=1)
    vizinho = _modelo.kneighbors(vetor, n_neighbors=1, return_distance=False)[0][0]
    rotulo = _rotulos_treinamento[vizinho]
    confianca = max(0.0, 1.0 - distancia[0][0])
    return rotulo, confianca


def responder_com_aprendizado(pergunta, confianca_minima=0.32):
    """Classifica uma pergunta e retorna uma resposta quando houver confiança."""
    rotulo, confianca = classificar_intencao(pergunta)

    if rotulo is None or confianca < confianca_minima:
        return None

    return RESPOSTAS_ML[rotulo]


def registrar_aprendizado(pergunta):
    """Salva uma confirmação do usuário e atualiza o modelo em memória."""
    rotulo, confianca = classificar_intencao(pergunta)
    if rotulo is None or confianca < 0.32:
        return False

    aprendidos = []
    if ARQUIVO_APRENDIZADO.exists():
        try:
            aprendidos = json.loads(ARQUIVO_APRENDIZADO.read_text(encoding="utf-8"))
        except (OSError, ValueError, TypeError):
            aprendidos = []

    if not any(item.get("pergunta") == pergunta for item in aprendidos):
        aprendidos.append({"pergunta": pergunta, "rotulo": rotulo})
        ARQUIVO_APRENDIZADO.write_text(
            json.dumps(aprendidos, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        _treinar()
    return True
