DIAS = [
    ("A presença do Pai", "Reconheça que Deus está perto. Ore com sinceridade e agradeça por sua presença.", "Tiago 4:8"),
    ("Um coração disponível", "Separe alguns minutos em silêncio para ouvir e entregar suas preocupações a Deus.", "Salmos 46:10"),
    ("Conhecer o caráter de Deus", "Leia sobre a bondade e a fidelidade de Deus. Anote uma característica que deseja conhecer melhor.", "Êxodo 34:6"),
    ("Filho amado", "Rejeite a ideia de que seu valor depende do desempenho. Receba o amor do Pai.", "1 João 3:1"),
    ("Confiança", "Entregue ao Pai uma preocupação concreta e dê hoje um passo responsável.", "Provérbios 3:5-6"),
    ("Gratidão", "Liste três coisas pelas quais você agradece, inclusive uma pequena bênção do dia.", "1 Tessalonicenses 5:18"),
    ("Arrependimento", "Reconheça um erro sem se condenar. Peça perdão e escolha uma mudança possível.", "1 João 1:9"),
    ("Perdão recebido", "Descanse na misericórdia de Deus e abandone a culpa que já foi confessada.", "Romanos 8:1"),
    ("Oração simples", "Fale com Deus como você está, sem discursos. Seja honesto sobre sentimentos e necessidades.", "Salmos 62:8"),
    ("A Palavra", "Leia um pequeno trecho bíblico devagar e pergunte: o que isso ensina sobre Deus e sobre mim?", "Salmos 119:105"),
    ("Obediência", "Escolha uma orientação que você já conhece e coloque-a em prática hoje.", "João 14:15"),
    ("Paciência", "Aceite que crescimento espiritual leva tempo. Faça o bem possível sem exigir resultados imediatos.", "Gálatas 6:9"),
    ("Descanso", "Pare por alguns minutos. O Pai não mede seu valor pela quantidade de tarefas concluídas.", "Mateus 11:28"),
    ("Ansiedade", "Entregue cada preocupação em oração e procure apoio confiável se ela estiver pesada demais.", "Filipenses 4:6-7"),
    ("Coragem", "Enfrente uma tarefa adiada com a certeza de que não está sozinho.", "Josué 1:9"),
    ("Sabedoria", "Antes de decidir, ore, reúna informações e peça conselho a pessoas maduras.", "Tiago 1:5"),
    ("Humildade", "Admita o que não sabe e esteja disposto a aprender com Deus e com outras pessoas.", "Provérbios 11:2"),
    ("Amor ao próximo", "Faça uma atitude concreta de cuidado sem esperar reconhecimento.", "João 13:34-35"),
    ("Respeito", "Escute alguém com atenção e responda sem humilhar, mesmo em uma discordância.", "Romanos 12:10"),
    ("Serviço", "Use uma habilidade sua para ajudar alguém de maneira prática.", "Gálatas 5:13"),
    ("Generosidade", "Compartilhe tempo, atenção ou recursos com responsabilidade e alegria.", "2 Coríntios 9:7"),
    ("Contentamento", "Observe o que já recebeu sem deixar de trabalhar por melhorias honestas.", "Filipenses 4:11-13"),
    ("Trabalho com propósito", "Faça sua tarefa de hoje com dedicação, integridade e cuidado.", "Colossenses 3:23"),
    ("Relacionamentos", "Procure reconciliação onde for seguro e estabeleça limites onde for necessário.", "Romanos 12:18"),
    ("Palavras", "Troque uma crítica impulsiva por uma palavra verdadeira e edificante.", "Efésios 4:29"),
    ("Domínio próprio", "Adie uma reação impulsiva, respire e escolha uma resposta coerente com seus valores.", "Provérbios 16:32"),
    ("Esperança", "Lembre-se de que um dia difícil não define toda a sua história.", "Lamentações 3:22-23"),
    ("Recomeço", "Comece novamente em uma área pequena, sem esperar perfeição.", "Isaías 43:19"),
    ("Identidade", "Escreva três qualidades que Deus pode desenvolver em você e uma atitude para cultivá-las.", "Efésios 2:10"),
    ("Proteção", "Ore por discernimento e mantenha distância de situações e pessoas que colocam você em risco.", "Salmos 121:7-8"),
    ("Justiça", "Seja honesto em uma escolha que ninguém está vendo.", "Miquéias 6:8"),
    ("Verdade", "Diga a verdade com amor, sem usar sinceridade como desculpa para ferir.", "Efésios 4:15"),
    ("Fé em ação", "Transforme uma oração em uma atitude responsável e possível.", "Tiago 2:17"),
    ("Comunidade", "Converse com uma pessoa de confiança sobre sua caminhada e aceite ajuda.", "Hebreus 10:24-25"),
    ("Consolo", "Permita-se receber cuidado em um momento de dor. Você não precisa sofrer isolado.", "Salmos 34:18"),
    ("Celebração", "Reconheça um pequeno avanço e agradeça ao Pai por ele.", "Salmos 126:3"),
    ("Direção", "Revise suas prioridades e escolha o próximo passo com calma.", "Salmos 25:4-5"),
    ("Perseverança", "Continue uma prática boa mesmo que o progresso pareça lento.", "Romanos 5:3-4"),
    ("Silêncio e escuta", "Fique em silêncio por alguns minutos e entregue a Deus a necessidade de controlar tudo.", "1 Reis 19:11-12"),
    ("Entrega", "Confie ao Pai o que você não pode controlar e cuide fielmente do que está ao seu alcance.", "1 Pedro 5:7"),
    ("Uma vida com Deus", "Continue a caminhada com oração, Palavra, amor, serviço e comunhão. A intimidade cresce diariamente.", "João 15:4-5"),
]


def plano_completo():
    return "40 Dias de Intimidade com Deus Pai\n\n" + "\n".join(
        f"Dia {numero}: {titulo} - {referencia}"
        for numero, (titulo, _, referencia) in enumerate(DIAS, 1)
    ) + "\n\nLeia o tema, ore com sinceridade e pratique a ação do dia."


def dia_do_plano(numero):
    if not 1 <= numero <= len(DIAS):
        return "Escolha um dia entre 1 e 40."
    titulo, pratica, referencia = DIAS[numero - 1]
    return f"Dia {numero}: {titulo}\n\n{pratica}\n\nLeia: {referencia}"
