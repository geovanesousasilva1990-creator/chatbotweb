from modelo_ml import responder_com_aprendizado
from devocional_40_dias import dia_do_plano, plano_completo

RESPOSTA_PADRAO = "Desculpe, sou especializado em temas bíblicos. Você poderia fazer uma pergunta sobre a Bíblia, Jesus, os Apóstolos, ou algum personagem e tema das Sagradas Escrituras?"


def responder(pergunta):

    pergunta = pergunta.lower().strip()

    if not pergunta:
        return "Digite uma pergunta sobre a Bíblia ou a fé cristã."

    if ("40 dias" in pergunta
            or "intimidade com deus pai" in pergunta
            or ("devocional" in pergunta and "dia" in pergunta)):
        import re
        dia = re.search(r"dia\s*(\d+)", pergunta)
        if dia:
            return dia_do_plano(int(dia.group(1)))
        return plano_completo()

    if "primeiro livro da biblia" in pergunta or "primeiro livro da bíblia" in pergunta:
        return "O primeiro livro da Bíblia é Gênesis. Ele fala sobre a criação, o início da humanidade e os primórdios da história da salvação."

    if "apóstolo" in pergunta or "apostolo" in pergunta or "discípulo" in pergunta or "discipulo" in pergunta:
        return "Jesus chamou doze apóstolos para anunciar o Reino de Deus: Pedro, João, Tiago, André, Filipe, Bartolomeu, Mateus, Tomé, Tiago filho de Alfeu, Tadeu, Simão e Judas Iscariotes. Os Evangelhos mostram que eles aprenderam com Jesus e foram enviados a testemunhar sua mensagem."

    if "livro da biblia" in pergunta or "livro da bíblia" in pergunta:
        return "A Bíblia tem 66 livros, sendo 39 no Antigo Testamento e 27 no Novo Testamento. Se quiser, posso listar todos os livros ou explicar qualquer um deles."

    resposta_ml = responder_com_aprendizado(pergunta)
    if resposta_ml:
        return resposta_ml

    # Saudações
    if "oi" in pergunta or "olá" in pergunta or "opa" in pergunta:
        return "Olá! Bem-vindo! Sou Geovane, um chatbot especializado em Bíblia. O que você gostaria de saber sobre a Sagrada Escritura?"

    elif "nome" in pergunta:
        return "Meu nome é Geovane. Posso ajudar com dúvidas bíblicas e mensagens de fé."

    # Jesus e vida cristã
    elif "jesus" in pergunta:
        return "Jesus é o Filho de Deus e nosso Salvador. 'Pois em nenhum outro há salvação' (Atos 4:12)."

    elif "salvador" in pergunta or "salvação" in pergunta:
        return "A salvação vem por Cristo. 'Porque Deus amou o mundo...' (João 3:16)."

    # Livros e personagens principais
    elif "gênesis" in pergunta or "adão" in pergunta:
        return "Gênesis é o começo. Ele mostra a criação e a graça de Deus desde o princípio."

    elif "moisés" in pergunta or "êxodo" in pergunta:
        return "Moisés foi usado por Deus para libertar Israel. 'E o Senhor disse: Eu sou o que sou' (Êxodo 3:14)."

    elif "davi" in pergunta or "salmos" in pergunta:
        return "Davi foi rei e poeta. 'O Senhor é o meu pastor' (Salmo 23:1)."

    elif "maria" in pergunta or "virgem" in pergunta:
        return "Maria foi escolhida por Deus para ser mãe de Jesus. 'Eis aqui a serva do Senhor' (Lucas 1:38)."

    # Conceitos cristianos
    elif "graça" in pergunta:
        return "Graça é o favor de Deus. 'Pela graça sois salvos, por meio da fé' (Efésios 2:8)."

    elif "fé" in pergunta:
        return "Fé é confiar em Deus. 'Ora, a fé é a certeza de coisas que se esperam' (Hebreus 11:1)."

    elif "amor" in pergunta:
        return "O amor é o maior mandamento. 'Deus é amor' (1 João 4:8)."

    elif "perdão" in pergunta:
        return "Deus perdoa ao que se arrepende. 'Se confessarmos os nossos pecados, ele é fiel e justo' (1 João 1:9)."

    # Eventos importantes
    elif "natal" in pergunta or "nascimento" in pergunta:
        return "Jesus nasceu em Belém. 'Hoje nasceu-vos o Salvador' (Lucas 2:11)."

    elif "páscoa" in pergunta or "ressurreição" in pergunta:
        return "A ressurreição é a vitória de Cristo. 'Se Cristo não ressuscitou, vossa fé é vã' (1 Coríntios 15:17)."

    elif "pentecostes" in pergunta:
        return "No Pentecostes, o Espírito Santo veio sobre os discípulos. 'Recebereis poder...' (Atos 1:8)."

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
        return "A Bíblia fala que Deus preparou um lugar para os que O amam. 'Na casa de meu Pai há muitas moradas' (João 14:2)."

    elif "inferno" in pergunta:
        return "O inferno é a separação eterna de Deus. A Bíblia nos exorta a aceitar Jesus para não sofrer essa condenação."

    elif "satanás" in pergunta or "demônio" in pergunta or "diabo" in pergunta:
        return "Satanás é o inimigo de Deus e da humanidade. Ele busca nos afastar de Deus, mas Jesus venceu Satanás na cruz."

    elif "oração" in pergunta:
        return "Oração é falar com Deus com confiança. 'Não andeis ansiosos...' (Filipenses 4:6-7)."

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
        return RESPOSTA_PADRAO


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