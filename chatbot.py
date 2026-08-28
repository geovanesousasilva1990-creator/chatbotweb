from modelo_ml import responder_com_aprendizado
from devocional_40_dias import dia_do_plano, plano_completo


def responder(pergunta):

    pergunta = pergunta.lower()

    if ("40 dias" in pergunta
            or "intimidade com deus pai" in pergunta
            or ("devocional" in pergunta and "dia" in pergunta)):
        import re
        dia = re.search(r"dia\s*(\d+)", pergunta)
        if dia:
            return dia_do_plano(int(dia.group(1)))
        return plano_completo()

    resposta_ml = responder_com_aprendizado(pergunta)
    if resposta_ml:
        return resposta_ml

    # Saudações
    if "oi" in pergunta or "olá" in pergunta or "opa" in pergunta:
        return "Olá! Bem-vindo! Sou Geovane, um chatbot especializado em Bíblia. O que você gostaria de saber sobre a Sagrada Escritura?"

    elif "nome" in pergunta:
        return "Meu nome é Geovane, sou um chatbot criado para responder perguntas sobre a Bíblia."

    # Jesus e vida cristã
    elif "jesus" in pergunta:
        return "Jesus é o Filho de Deus, nosso Salvador. Nasceu em Belém, ministrou por aproximadamente 3 anos, e morreu na cruz para redimir a humanidade. Ressuscitou ao terceiro dia!"

    elif "salvador" in pergunta or "salvação" in pergunta:
        return "A salvação em Cristo significa ter os pecados perdoados e receber vida eterna. João 3:16 diz: 'Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna.'"

    # Livros e personagens principais
    elif "gênesis" in pergunta or "adão" in pergunta:
        return "Gênesis é o primeiro livro da Bíblia. Conta a criação do mundo, Adão e Eva no Éden, o dilúvio, e a história de Noé e Abraão."

    elif "moisés" in pergunta or "êxodo" in pergunta:
        return "Moisés foi o grande líder do povo de Israel. Recebeu os Dez Mandamentos no Monte Sinai e guiou os israelitas pela jornada de 40 anos no deserto."

    elif "davi" in pergunta or "salmos" in pergunta:
        return "Davi foi o grande rei de Israel e escreveu muitos Salmos. Venceu Golias ainda jovem, e sua linhagem levou a Jesus Cristo."

    elif "maria" in pergunta or "virgem" in pergunta:
        return "Maria foi a mãe de Jesus. Escolhida por Deus para uma missão especial, ela é venerada como a mãe do Redentor."

    # Conceitos cristianos
    elif "graça" in pergunta:
        return "Graça é a misericórdia e favor de Deus para conosco, que não merecemos. É pela graça de Deus que somos salvos, não por nossas obras."

    elif "fé" in pergunta:
        return "Fé é crer em Deus e em Suas promessas. Hebreus 11:1 diz: 'Ora, a fé é a certeza de coisas que se espera, a convicção de fatos que se não veem.'"

    elif "amor" in pergunta:
        return "O amor é o maior mandamento. 1 João 4:8 diz: 'Aquele que não ama não conhece a Deus; porque Deus é amor.'"

    elif "perdão" in pergunta:
        return "Deus nos perdoa quando nos arrependemos sinceramente de nossos pecados. Ele oferece perdão através da morte e ressurreição de Jesus Cristo."

    # Eventos importantes
    elif "natal" in pergunta or "nascimento" in pergunta:
        return "Jesus nasceu em Belém, em um estábulo. Os pastores foram os primeiros a saber da Sua vinda, seguidos pelos três reis magos do Oriente."

    elif "páscoa" in pergunta or "ressurreição" in pergunta:
        return "A Páscoa celebra a ressurreição de Jesus Cristo ao terceiro dia após Sua crucificação. É o evento mais importante da fé cristã, pois garante nossa salvação."

    elif "pentecostes" in pergunta:
        return "Pentecostes foi quando o Espírito Santo desceu sobre os discípulos de Jesus em Jerusalém, capacitando-os a pregar o Evangelho em diferentes línguas."

    # Dez Mandamentos
    elif "mandamento" in pergunta:
        return "Os Dez Mandamentos foram dados por Deus a Moisés no Monte Sinai. Resumem-se em amar a Deus de todo coração e amar o próximo como a si mesmo."

    # Testamentos
    elif "antigo testamento" in pergunta or "velho testamento" in pergunta:
        return "O Antigo Testamento contém 39 livros da Bíblia hebraica, narrando a história de Israel desde a criação até a vinda do Messias."

    elif "novo testamento" in pergunta:
        return "O Novo Testamento contém 27 livros, incluindo os 4 Evangelhos (Mateus, Marcos, Lucas e João), os Atos, as cartas de Paulo e de outros apóstolos, e o Apocalipse."

    elif "evangelho" in pergunta:
        return "Os Evangelhos são os 4 livros que narram a vida, ensinamentos, morte e ressurreição de Jesus: Mateus, Marcos, Lucas e João."

    # Apóstolos e discípulos
    elif "pedro" in pergunta:
        return "Pedro foi um dos apóstolos de Jesus. Jesus disse a ele: 'Tu és Pedro, e sobre esta pedra edificarei a minha igreja.' Ele foi importante na formação da Igreja Cristã."

    elif "paulo" in pergunta or "saulo" in pergunta:
        return "Paulo (antes chamado Saulo) foi um grande apóstolo que se converteu a Cristo. Escreveu muitas cartas que formam grande parte do Novo Testamento."

    elif "apóstolos" in pergunta or "discípulos" in pergunta:
        return "Jesus escolheu 12 apóstolos para pregarem o Evangelho. São eles: Pedro, Tiago, João, André, Filipe, Bartolomeu, Mateus, Tomé, Tiago (o Menor), Judas Tadeu, Simão e Judas Iscariotes."

    # Milagres
    elif "milagre" in pergunta:
        return "Jesus realizou muitos milagres: transformou água em vinho, curou enfermos, acalmou a tempestade, alimentou multidões e ressuscitou mortos. Tudo para demonstrar Seu poder e compaixão."

    # Outros tópicos
    elif "céu" in pergunta or "paraíso" in pergunta:
        return "O Céu é o lugar preparado por Deus para os que creem em Jesus Cristo. É um lugar de felicidade eterna, sem sofrimento nem morte."

    elif "inferno" in pergunta:
        return "O inferno é a separação eterna de Deus. A Bíblia nos exorta a aceitar Jesus para não sofrer essa condenação."

    elif "satanás" in pergunta or "demônio" in pergunta or "diabo" in pergunta:
        return "Satanás é o inimigo de Deus e da humanidade. Ele busca nos afastar de Deus, mas Jesus venceu Satanás na cruz."

    elif "oração" in pergunta:
        return "Oração é comunicação com Deus. Podemos apresentar nossos pedidos, agradecimentos e intercessões a Deus através da oração. Jesus nos ensinou o Pai Nosso como modelo."

    elif "livros da bíblia" in pergunta or "livros da biblia" in pergunta:
        return ("A Bíblia tem 66 livros na tradição protestante.\n\n"
                "Antigo Testamento (39): Gênesis, Êxodo, Levítico, Números, "
                "Deuteronômio, Josué, Juízes, Rute, 1 Samuel, 2 Samuel, 1 Reis, "
                "2 Reis, 1 Crônicas, 2 Crônicas, Esdras, Neemias, Ester, Jó, "
                "Salmos, Provérbios, Eclesiastes, Cânticos, Isaías, Jeremias, "
                "Lamentações, Ezequiel, Daniel, Oséias, Joel, Amós, Obadias, "
                "Jonas, Miquéias, Naum, Habacuque, Sofonias, Ageu, Zacarias e Malaquias.\n\n"
                "Novo Testamento (27): Mateus, Marcos, Lucas, João, Atos, Romanos, "
                "1 Coríntios, 2 Coríntios, Gálatas, Efésios, Filipenses, Colossenses, "
                "1 Tessalonicenses, 2 Tessalonicenses, 1 Timóteo, 2 Timóteo, Tito, "
                "Filemom, Hebreus, Tiago, 1 Pedro, 2 Pedro, 1 João, 2 João, 3 João, "
                "Judas e Apocalipse.")

    elif "bíblia" in pergunta or "biblia" in pergunta or "sagrada escritura" in pergunta:
        return "A Bíblia é a palavra de Deus, dividida em Antigo e Novo Testamento. Contém 66 livros que orientam nossa fé e vida cristã."

    else:
        return "Desculpe, sou especializado em temas bíblicos. Você poderia fazer uma pergunta sobre a Bíblia, Jesus, os Apóstolos, ou algum personagem e tema das Sagradas Escrituras?"


def buscar_versiculo(texto):
    """Busca uma referência bíblica na Bible API."""
    import re
    import unicodedata

    import requests

    livros = {
        "genesis": "Genesis", "exodo": "Exodus", "levitico": "Leviticus",
        "numeros": "Numbers", "deuteronomio": "Deuteronomy", "josue": "Joshua",
        "juizes": "Judges", "rute": "Ruth", "1 samuel": "1 Samuel",
        "2 samuel": "2 Samuel", "1 reis": "1 Kings", "2 reis": "2 Kings",
        "1 cronicas": "1 Chronicles", "2 cronicas": "2 Chronicles",
        "esdras": "Ezra", "neemias": "Nehemiah", "ester": "Esther", "jo": "Job",
        "salmo": "Psalms", "salmos": "Psalms", "proverbios": "Proverbs",
        "eclesiastes": "Ecclesiastes", "canticos": "Canticles",
        "cantico dos canticos": "Canticles", "cântico dos cânticos": "Canticles",
        "isaias": "Isaiah", "jeremias": "Jeremiah",
        "lamentacoes": "Lamentations", "ezequiel": "Ezekiel", "daniel": "Daniel",
        "oseias": "Hosea", "joel": "Joel", "amos": "Amos", "obadias": "Obadiah",
        "jonas": "Jonah", "miqueias": "Micah", "naum": "Nahum",
        "habacuque": "Habakkuk", "sofonias": "Zephaniah", "ageu": "Haggai",
        "zacarias": "Zechariah", "malaquias": "Malachi", "mateus": "Matthew",
        "marcos": "Mark", "lucas": "Luke", "joao": "John", "atos": "Acts",
        "romanos": "Romans", "1 corintios": "1 Corinthians", "2 corintios": "2 Corinthians",
        "galatas": "Galatians", "efesios": "Ephesians", "filipenses": "Philippians",
        "colossenses": "Colossians", "1 tessalonicenses": "1 Thessalonians",
        "2 tessalonicenses": "2 Thessalonians", "1 timoteo": "1 Timothy",
        "2 timoteo": "2 Timothy", "tito": "Titus", "filemom": "Philemon",
        "hebreus": "Hebrews", "tiago": "James", "1 pedro": "1 Peter",
        "2 pedro": "2 Peter", "1 joao": "1 John", "2 joao": "2 John",
        "3 joao": "3 John", "judas": "Jude", "apocalipse": "Revelation",
        "revelacao": "Revelation"
    }

    def sem_acento(valor):
        return "".join(
            caractere for caractere in unicodedata.normalize("NFD", valor.lower())
            if unicodedata.category(caractere) != "Mn"
        )

    texto_normalizado = sem_acento(texto)
    padrao = re.search(
        r"((?:[1-3]\s*)?[a-z]+(?:\s+[a-z]+)?)\s+(\d+)(?::(\d+)(?:-(\d+))?)?",
        texto_normalizado,
    )
    if not padrao:
        return None

    livro = livros.get(padrao.group(1).strip())
    if not livro:
        return None

    capitulo = padrao.group(2)
    inicio = padrao.group(3)
    fim = padrao.group(4)
    referencia = f"{livro}+{capitulo}"
    if inicio:
        referencia += f":{inicio}"
        if fim:
            referencia += f"-{fim}"

    try:
        resposta = requests.get(
            f"https://bible-api.com/{referencia}?translation=almeida",
            timeout=8,
        )
        resposta.raise_for_status()
        versiculos = resposta.json().get("verses", [])
        if not versiculos:
            return None

        texto_versiculos = " ".join(
            versiculo.get("text", "").strip() for versiculo in versiculos
        )
        referencia_exibida = resposta.json().get("reference", referencia.replace("+", " "))
        return f"📖 {referencia_exibida}\n\n\"{texto_versiculos}\""
    except (requests.RequestException, ValueError, KeyError):
        return None