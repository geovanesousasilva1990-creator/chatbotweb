import json
import unicodedata
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from database import registrar_resposta

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

LIVROS_BIBLIA = [
    "Gênesis", "Êxodo", "Levítico", "Números", "Deuteronômio",
    "Josué", "Juízes", "Rute", "1 Samuel", "2 Samuel", "1 Reis", "2 Reis",
    "1 Crônicas", "2 Crônicas", "Esdras", "Neemias", "Ester", "Jó",
    "Salmos", "Provérbios", "Eclesiastes", "Cânticos", "Isaías",
    "Jeremias", "Lamentações", "Ezequiel", "Daniel", "Oséias", "Joel",
    "Amós", "Obadias", "Jonas", "Miquéias", "Naum", "Habacuque",
    "Sofonias", "Ageu", "Zacarias", "Malaquias", "Mateus", "Marcos",
    "Lucas", "João", "Atos", "Romanos", "1 Coríntios", "2 Coríntios",
    "Gálatas", "Efésios", "Filipenses", "Colossenses", "1 Tessalonicenses",
    "2 Tessalonicenses", "1 Timóteo", "2 Timóteo", "Tito", "Filemom",
    "Hebreus", "Tiago", "1 Pedro", "2 Pedro", "1 João", "2 João",
    "3 João", "Judas", "Apocalipse"
]

LIVRO_SLUGS = {
    livro: livro.lower().replace(" ", "_").replace("-", "_").replace("ã", "a").replace("á", "a").replace("à", "a").replace("â", "a").replace("é", "e").replace("ê", "e").replace("í", "i").replace("ó", "o").replace("ô", "o").replace("ú", "u").replace("ç", "c")
    for livro in LIVROS_BIBLIA
}

DEVOCIONAIS = {
    "o salvador chegou": (
        "O Salvador Chegou\n\n"
        "Leitura: A chegada de Jesus revela que Deus não ficou distante da humanidade. "
        "Em Cristo encontramos graça, reconciliação e uma nova direção para a vida.\n\n"
        "Leia: Lucas 2:10-11.\n"
        "Pratique: agradeça a Deus pela salvação e demonstre hoje uma atitude de amor."
    ),
    "nome sobre todo nome": (
        "Nome Sobre Todo Nome\n\n"
        "Leitura: O nome de Jesus aponta para sua autoridade, humildade e vitória. "
        "Honrar esse nome também significa seguir seu exemplo no modo de tratar as pessoas.\n\n"
        "Leia: Filipenses 2:9-11.\n"
        "Pratique: escolha uma atitude de humildade e serviço para realizar hoje."
    ),
    "devocionais das maravilhas": (
        "Devocionais das Maravilhas\n\n"
        "Leitura: A criação, a providência e a transformação de vidas lembram que Deus continua "
        "agindo com sabedoria. Observe as pequenas bênçãos sem deixar de enfrentar a realidade com fé.\n\n"
        "Leia: Salmos 111:2-4.\n"
        "Pratique: anote três sinais de bondade que você percebeu hoje."
    ),
    "você está com medo": (
        "Você Está com Medo\n\n"
        "Leitura: O medo pode ser reconhecido sem comandar nossas decisões. Deus oferece presença, "
        "sabedoria e apoio para o próximo passo.\n\n"
        "Leia: Salmos 56:3-4.\n"
        "Pratique: respire com calma, ore e converse com alguém de confiança sobre o que preocupa você."
    ),
    "99 sermões para vida com deus": (
        "99 Sermões para Vida com Deus\n\n"
        "Leitura: Uma vida com Deus é construída na constância: ouvir a Palavra, refletir e praticar. "
        "Conhecimento bíblico se torna maturidade quando produz amor e justiça.\n\n"
        "Leia: Tiago 1:22.\n"
        "Pratique: transforme um ensinamento que você leu em uma ação concreta."
    ),
    "devocionais bíblicos gratuitos": (
        "Devocionais Bíblicos Gratuitos\n\n"
        "Leitura: A Palavra pode acompanhar todos os dias, em momentos simples e sinceros. "
        "Não é a quantidade de páginas, mas a disposição de escutar e viver com propósito.\n\n"
        "Leia: Salmos 119:105.\n"
        "Pratique: separe dez minutos sem distrações para ler e orar."
    ),
    "devocional diário 30 dias com deus": (
        "Devocional Diário: 30 Dias com Deus\n\n"
        "Leitura: A constância transforma pequenos momentos em uma caminhada. Comece com o que é "
        "possível hoje, sem transformar a disciplina espiritual em culpa.\n\n"
        "Leia: Lamentações 3:22-23.\n"
        "Pratique: defina um horário realista para voltar à leitura amanhã."
    ),
    "guia devocional de 21 dias para jejum e oração": (
        "Guia Devocional de 21 Dias para Jejum e Oração\n\n"
        "Leitura: Jejum não é uma forma de pressionar Deus, mas uma prática de atenção, oração e "
        "dependência. Faça com responsabilidade e não prejudique sua saúde.\n\n"
        "Leia: Isaías 58:6-9.\n"
        "Pratique: troque um período de distração por oração e uma atitude de misericórdia."
    ),
    "devocional a forja crescimento espiritual": (
        "Devocional A Forja: Crescimento Espiritual\n\n"
        "Leitura: O crescimento espiritual inclui ser moldado com paciência, correção e esperança. "
        "Dificuldades podem ensinar perseverança quando enfrentadas com apoio e sabedoria.\n\n"
        "Leia: Romanos 5:3-5.\n"
        "Pratique: identifique uma virtude que deseja desenvolver e dê um pequeno passo hoje."
    ),
    "devocional de 21 dias para negócios": (
        "Devocional de 21 Dias para Negócios\n\n"
        "Leitura: A fé também orienta o trabalho: honestidade, responsabilidade, serviço e cuidado "
        "com as pessoas. Sucesso não deve ser separado de integridade.\n\n"
        "Leia: Provérbios 11:1-3.\n"
        "Pratique: tome uma decisão profissional hoje com transparência e respeito."
    ),
}

DEVOCIONAIS_TITULOS = {
    titulo: texto.split("\n\n", 1)[0]
    for titulo, texto in DEVOCIONAIS.items()
}


def listar_devocionais():
    return [
        {
            "titulo": texto,
            "leitura": DEVOCIONAIS[identificador],
        }
        for identificador, texto in DEVOCIONAIS_TITULOS.items()
    ]

EXEMPLOS.extend((livro, LIVRO_SLUGS[livro]) for livro in LIVROS_BIBLIA)

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
    "livros_biblia": "A Bíblia tem 66 livros na tradição protestante: 39 no Antigo Testamento e 27 no Novo Testamento. Posso te mostrar a lista completa e explicar qualquer livro que você quiser conhecer.",
    "antigo_testamento": "O Antigo Testamento reúne 39 livros na tradição protestante, desde Gênesis até Malaquias. Ele narra a criação, a aliança e a preparação para a vinda do Messias.",
    "novo_testamento": "O Novo Testamento reúne 27 livros, começando por Mateus e terminando em Apocalipse. Ele conta a vida de Jesus, a igreja primitiva e a esperança final.",
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
    "genesis": "Gênesis é o primeiro livro da Bíblia e relata a criação do mundo, a queda do homem e a história dos patriarcas, começando com Adão e Eva e seguindo com Abraão e seus descendentes.",
    "exodo": "Êxodo narra a saída do povo de Israel do Egito, a liderança de Moisés, e a entrega dos Dez Mandamentos no monte Sinai.",
    "levitico": "Levítico apresenta as leis de purificação, sacrifícios, culto e a santidade de Deus, mostrando como o povo deveria viver diante do Senhor.",
    "numeros": "Números continua a jornada do povo de Israel pelo deserto, mostrando suas lutas, murmurações e a fidelidade de Deus mesmo em meio às falhas humanas.",
    "deuteronomio": "Deuteronômio é a recapitulada dos mandamentos de Deus e a chamada para que o povo escolha obedecer ao Senhor e viver em compromisso com Ele.",
    "josue": "Josué narra a entrada de Israel na Terra Prometida e a conquista das cidades, mostrando a fidelidade de Deus ao cumprir suas promessas.",
    "juizes": "Juízes mostra um ciclo de apostasia, opressão, clamor e redenção, destacando a necessidade de um líder que confie em Deus.",
    "rute": "Rute é um lindo livro de fidelidade, amor e provisão, mostrando como a graça de Deus atua na vida de uma mulher moabita que se torna parte da linhagem messiânica.",
    "1_samuel": "1 Samuel conta a história da unção de Saul e Davi, mostrando como Deus escolhe a pessoa certa e trabalha por um propósito maior.",
    "2_samuel": "2 Samuel continua a história de Davi, seu reinado, seus triunfos e suas falhas, revelando que Deus honra o coração que busca a Sua vontade.",
    "1_reis": "1 Reis narra a divisão do reino, o reinado dos reis de Israel e Judá, e as consequências da apostasia e da desobediência.",
    "2_reis": "2 Reis acompanha a história dos reis após a divisão do reino, mostrando a queda de Israel e Judá e o cumprimento das promessas de Deus.",
    "1_cronicas": "1 Crônicas retoma a história de Israel com foco na linhagem real e na adoração a Deus, exaltando a soberania do Senhor.",
    "2_cronicas": "2 Crônicas destaca os reis, o templo e a importância da fidelidade, mostrando que a restauração do povo começa na adoração verdadeira.",
    "esdras": "Esdras fala sobre a restauração do povo de Deus após o cativeiro, enfatizando a volta à Palavra, à obediência e à reconstrução espiritual.",
    "neemias": "Neemias mostra a reconstrução das muralhas de Jerusalém e a coragem de um homem que orou, liderou e perseverou em tempos difíceis.",
    "ester": "Ester é a história da coragem e da providência de Deus em um contexto de perigo, mostrando como o Senhor atua mesmo quando não vemos a sua mão imediatamente.",
    "jo": "Jó apresenta a questão do sofrimento e da soberania de Deus, ensinando que o Senhor conhece o plano maior, mesmo quando não entendemos o momento.",
    "salmos": "Salmos é o livro da oração, do louvor, do sofrimento e da esperança, trazendo palavras para toda situação da vida humana.",
    "proverbios": "Provérbios reúne sabedoria prática para viver com discernimento, humildade, honestidade e temor ao Senhor.",
    "eclesiastes": "Eclesiastes reflete sobre a vida, a vaidade, o propósito e a busca de sentido, mostrando que Deus é a resposta para o coração humano.",
    "canticos": "Cânticos é um poema de amor e devoção, representando a beleza do relacionamento, do compromisso e do afeto em um contexto bíblico.",
    "isaias": "Isaías anuncia juízo, esperança e a chegada do Messias, revelando a glória de Deus e o plano de redenção para o mundo.",
    "jeremias": "Jeremias é conhecido como o profeta das lamentações, falando sobre juízo, arrependimento e o novo coração que Deus prometeu.",
    "lamentacoes": "Lamentações expressa profunda dor e tristeza, mas também aponta para a misericórdia de Deus que se renova de manhã.",
    "ezequiel": "Ezequiel revela visões de juízo, restauração e a presença de Deus, mostrando que o Senhor é fiel mesmo no meio da crise.",
    "daniel": "Daniel destaca fidelidade em meio à pressão, sonhos e visões sobre o futuro, e a soberania de Deus sobre os reis e impérios.",
    "oseias": "Oséias mostra o amor de Deus por um povo infiel, revelando a graça, o perdão e o cuidado do Senhor com o seu povo.",
    "joel": "Joel fala sobre juízo, arrependimento e a promessa do Espírito Santo derramado sobre toda a carne.",
    "amos": "Amós denuncia a injustiça e a hipocrisia, convidando o povo a viver a justiça e a verdade.",
    "obadias": "Obadias traz uma mensagem sobre a soberania de Deus sobre as nações e a justiça final que Ele exercerá.",
    "jonas": "Jonas mostra a misericórdia de Deus, a importância do arrependimento e a graça que alcança até mesmo quem está distante.",
    "miqueias": "Miquéias anuncia juízo, mas também promete restauração e a esperança de um futuro de justiça e paz.",
    "naum": "Naum fala da justiça e da soberania de Deus diante das nações, mostrando que o Senhor não ignora a injustiça.",
    "habacuque": "Habacuque aborda as perguntas do coração diante da dor e da demora, ensinando a confiar na justiça de Deus.",
    "sofonias": "Sofonias fala sobre o dia do Senhor, o juízo e também a alegria de um povo que retorna ao Senhor.",
    "ageu": "Ageu incentiva a reconstrução do templo e a prioridade da casa do Senhor, lembrando que a obra de Deus exige fé e compromisso.",
    "zacarias": "Zacarias revela visões de esperança, restauração e a vinda do Messias, mostrando que Deus honra suas promessas.",
    "malaquias": "Malaquias conclui o Antigo Testamento com chamado ao arrependimento, à fidelidade e à esperança na vinda do Senhor.",
    "mateus": "Mateus apresenta Jesus como o Messias e o Rei, enfatizando o cumprimento das Escrituras e os ensinamentos de Jesus sobre o Reino de Deus.",
    "marcos": "Marcos é um Evangelho direto e cheio de ação, mostrando o ministério de Jesus com rapidez e autoridade.",
    "lucas": "Lucas destaca a compaixão de Jesus, a cura, a misericórdia e o cuidado de Deus para com os pequenos e marginalizados.",
    "joao": "João destaca a divindade de Jesus, os sinais que Ele realizou e a mensagem de vida, amor e verdade.",
    "atos": "Atos descreve a expansão da igreja primitiva, a obra do Espírito Santo e a pregação do Evangelho ao mundo.",
    "romanos": "Romanos é uma carta profunda sobre o pecado, a graça, a justiça de Deus e a salvação pela fé em Cristo.",
    "1_corintios": "1 Coríntios trata da vida da igreja, do amor, da disciplina, dos dons espirituais e da importância da ordem na comunidade cristã.",
    "2_corintios": "2 Coríntios fala sobre conforto, ministério, graça e a força de Deus manifestada na fraqueza humana.",
    "galatas": "Gálatas destaca a liberdade em Cristo, a justiça pela fé e a rejeição de qualquer legalismo que desvie do evangelho.",
    "efesios": "Efésios revela a riqueza espiritual do crente em Cristo e a chamada para viver em amor, unidade e santidade.",
    "filipenses": "Filipenses ensina alegria, humildade, perseverança e o exemplo de Jesus em meio a desafios e perseguições.",
    "colossenses": "Colossenses enfatiza a supremacia de Cristo e a importância de viver uma vida centrada no Senhor.",
    "1_tessalonicenses": "1 Tessalonicenses exorta a igreja a viver em santidade, perseverança e esperança na vinda de Cristo.",
    "2_tessalonicenses": "2 Tessalonicenses fala sobre a esperança da vinda de Cristo, a fidelidade da igreja e a necessidade de perseverança.",
    "1_timoteo": "1 Timóteo orienta sobre liderança, ensino, disciplina e a forma de viver uma vida piedosa e íntegra.",
    "2_timoteo": "2 Timóteo é uma carta de encorajamento para perseverar na fé, mesmo diante da oposição e do sofrimento.",
    "tito": "Tito ensina sobre a vida cristã, a prudência, a ordem da igreja e a importância de boas obras.",
    "filemom": "Filemom é uma carta breve sobre perdão, graça e a dignidade de cada pessoa em Cristo.",
    "hebreus": "Hebreus destaca a superioridade de Cristo, a fé e a perseverança, mostrando que a promessa de Deus é segura.",
    "tiago": "Tiago ensina fé em ação, humildade, sabedoria, justiça e a importância de viver de acordo com o que se crê.",
    "1_pedro": "1 Pedro encoraja o povo de Deus a perseverar em meio à tribulação, confiando na graça e na esperança de Cristo.",
    "2_pedro": "2 Pedro chama a igreja a crescer na fé, a evitar falsos ensinos e a viver em santidade.",
    "1_joao": "1 João fala sobre amor, verdade, fé e a certeza da vida em Cristo, mostrando que a comunhão com Deus transforma a vida.",
    "2_joao": "2 João é uma carta breve sobre amor, verdade e cuidado contra falsos ensinos.",
    "3_joao": "3 João ensina sobre hospitalidade, apoio mútuo e a importância de viver em verdade e amor.",
    "judas": "Judas chama a igreja a defender a fé, resistir ao erro e manter-se firme na graça de Deus.",
    "apocalipse": "Apocalipse revela a vitória final de Cristo, a soberania de Deus e a esperança da nova criação para os que permanecem fiéis.",
}

def normalizar_texto(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )


def resposta_devocional(pergunta):
    pergunta_normalizada = normalizar_texto(pergunta)
    for titulo, leitura in DEVOCIONAIS.items():
        if titulo in pergunta_normalizada:
            return leitura
    return None


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
    pergunta_normalizada = normalizar_texto(pergunta)
    for livro, slug in LIVRO_SLUGS.items():
        livro_normalizado = normalizar_texto(livro)
        if livro_normalizado in pergunta_normalizada or pergunta_normalizada in livro_normalizado:
            return slug, 0.99

    vetor = _vetorizador.transform([pergunta_normalizada])
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

    resposta = RESPOSTAS_ML[rotulo]
    registrar_resposta(pergunta, resposta, categoria="biblia", fonte="modelo_ml")
    return resposta


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
