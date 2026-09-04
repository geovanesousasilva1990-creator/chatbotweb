function enviar() {
    const mensagem = document.getElementById("mensagem").value.trim();
    const botao = document.getElementById("enviar");
    
    if (mensagem === "" || botao.disabled) return;

    const texto = mensagem.toLowerCase();
    if (texto === "silencio" || texto === "silêncio" || texto === "quieto" || texto === "calado") {
        vozAtivada = false;
        const botaoSom = document.getElementById("som");
        if (botaoSom) {
            botaoSom.textContent = "🔇\nOff";
            botaoSom.title = "Ativar voz";
        }
        if ("speechSynthesis" in window) {
            window.speechSynthesis.cancel();
            finalizarFala();
            adicionarMensagem("Silêncio ativado. A voz foi desligada.", "bot");
        }
        document.getElementById("mensagem").value = "";
        return;
    }
    
    // Exibir mensagem do usuário
    adicionarMensagem(mensagem, "usuario");
    document.getElementById("mensagem").value = "";
    botao.disabled = true;
    mostrarDigitando();
    
    // Enviar para o servidor
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ mensagem: mensagem })
    })
    .then(async response => {
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
            throw new Error(data.erro || "O servidor não conseguiu processar a pergunta.");
        }
        return data;
    })
    .then(data => {
        removerDigitando();
        adicionarMensagem(data.resposta, "bot", mensagem);
    })
    .catch(error => {
        removerDigitando();
        adicionarMensagem("Não consegui responder agora. Verifique sua conexão e tente novamente.", "bot");
        console.error("Erro:", error);
    })
    .finally(() => {
        botao.disabled = false;
        document.getElementById("mensagem").focus();
    });
}

function abrirBiblioteca() {
    fetch("/devocionais")
        .then(response => response.json())
        .then(data => {
            adicionarMensagem("Biblioteca de fé: escolha um livro para começar a leitura.", "bot");
            const conversa = document.getElementById("conversa");
            let categoriaAtual = "";
            data.devocionais.forEach(item => {
                if (item.categoria !== categoriaAtual) {
                    categoriaAtual = item.categoria;
                    const categoria = document.createElement("h3");
                    categoria.className = "categoria-biblioteca";
                    categoria.textContent = categoriaAtual;
                    conversa.appendChild(categoria);
                }
                const linha = document.createElement("div");
                linha.className = "item-biblioteca";
                const titulo = document.createElement("span");
                titulo.textContent = item.titulo;
                const ler = document.createElement("button");
                ler.type = "button";
                ler.textContent = "Ler";
                ler.title = `Ler ${item.titulo}`;
                ler.onclick = () => adicionarMensagem(item.leitura, "bot");
                linha.append(titulo, ler);
                conversa.appendChild(linha);
            });
            conversa.scrollTop = conversa.scrollHeight;
        })
        .catch(() => adicionarMensagem("Não consegui abrir a biblioteca agora. Tente novamente.", "bot"));
}

function mostrarDigitando() {
    const conversa = document.getElementById("conversa");
    const div = document.createElement("div");
    div.id = "digitando";
    div.className = "mensagem bot";
    div.setAttribute("aria-label", "O chatbot está digitando");
    div.innerHTML = '<span class="texto digitando"><i></i><i></i><i></i></span>';
    conversa.appendChild(div);
    conversa.scrollTop = conversa.scrollHeight;
}

function removerDigitando() {
    const indicador = document.getElementById("digitando");
    if (indicador) indicador.remove();
}

function adicionarMensagem(texto, tipo, pergunta = "") {
    const conversa = document.getElementById("conversa");
    
    const div = document.createElement("div");
    div.className = "mensagem " + tipo;
    
    const span = document.createElement("span");
    span.className = "texto";
    span.textContent = texto;
    
    div.appendChild(span);

    if (tipo === "bot") {
        const ouvir = document.createElement("button");
        ouvir.className = "ouvir";
        ouvir.type = "button";
        ouvir.textContent = "Ouvir";
        ouvir.title = "Ouvir resposta";
        ouvir.onclick = () => alternarVoz(texto, ouvir);
        div.appendChild(ouvir);

        if (pergunta) {
            const feedback = document.createElement("button");
            feedback.className = "feedback";
            feedback.type = "button";
            feedback.textContent = "Ajudou";
            feedback.onclick = () => registrarFeedback(pergunta, feedback);
            div.appendChild(feedback);
        }

        setTimeout(() => {
            if (vozAtivada && "speechSynthesis" in window && !botaoFalando) {
                const resposta = texto;
                alternarVoz(resposta, ouvir);
            }
        }, 300);
    }

    conversa.appendChild(div);
    
    // Scroll para o final
    conversa.scrollTop = conversa.scrollHeight;
}

let botaoFalando = null;
let filaDeFala = [];
let indiceDaFala = 0;
let vozAtivada = true;

function alternarSom() {
    vozAtivada = !vozAtivada;
    const botaoSom = document.getElementById("som");
    if (!botaoSom) return;

    botaoSom.textContent = vozAtivada ? "🔊\nA" : "🔇\nOff";
    botaoSom.title = vozAtivada ? "Desativar voz" : "Ativar voz";

    if (!vozAtivada && "speechSynthesis" in window) {
        window.speechSynthesis.cancel();
        finalizarFala();
    }
}

function textoParaVoz(texto) {
    return texto
        .replace(/[📖🎤🙏✝️💪📚💝]/g, "")
        .replace(/[*_`#>]/g, "")
        .replace(/\b(1|2|3)\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ])/g, "$1 ")
        .replace(/\bJoão\s+(\d+)/gi, "João capítulo $1")
        .replace(/\bSalmos\s+(\d+)/gi, "Salmos capítulo $1")
        .replace(/\b(\d+):(\d+)\b/g, "capítulo $1 versículo $2")
        .replace(/\([^)]*\)/g, "")
        .replace(/\s+/g, " ")
        .trim();
}

function vozBrasileira() {
    const vozes = window.speechSynthesis.getVoices();

    const vozesBrasileiras = vozes.filter(voz =>
        voz.lang.toLowerCase().startsWith("pt-br")
    );

    const vozesMasculinas = vozesBrasileiras.filter(voz =>
        /daniel|antonio|antônio|felipe|paulo|joao|joão|male|masculino/i.test(voz.name)
    );

    const vozExata = vozesMasculinas.find(voz => {
        const nome = voz.name.toLowerCase();
        return nome.includes("microsoft daniel")
            || nome.includes("microsoft paulo")
            || nome.includes("paulo");
    });

    if (vozExata) return vozExata;

    const preferidas = [
        "Microsoft Daniel",
        "Daniel",
        "Microsoft Antonio",
        "Microsoft Felipe",
        "Microsoft João",
        "João"
    ];

    return vozesMasculinas.find(voz => {
        const nome = voz.name.toLowerCase();
        return preferidas.some(p => nome.includes(p.toLowerCase()));
    })
        || vozesMasculinas[0]
        || vozes.find(voz => voz.lang.toLowerCase().startsWith("pt"));
}

function atualizarBotaoDeFala(botao, falando) {
    botao.textContent = falando ? "Parar" : "Ouvir";
    botao.classList.toggle("falando", falando);
}

function finalizarFala() {
    if (botaoFalando) atualizarBotaoDeFala(botaoFalando, false);
    botaoFalando = null;
    filaDeFala = [];
    indiceDaFala = 0;
}

function falarProximoTrecho(voz, botao) {
    if (indiceDaFala >= filaDeFala.length || botaoFalando !== botao) {
        finalizarFala();
        return;
    }

    const fala = new SpeechSynthesisUtterance(filaDeFala[indiceDaFala]);
    fala.lang = "pt-BR";
    fala.rate = 0.78;
    fala.pitch = 0.82;
    fala.volume = 1;
    if (voz) fala.voice = voz;
    fala.onend = () => {
        indiceDaFala += 1;
        falarProximoTrecho(voz, botao);
    };
    fala.onerror = finalizarFala;
    window.speechSynthesis.speak(fala);
}

function alternarVoz(texto, botao) {
    if (!("speechSynthesis" in window)) return;

    if (botaoFalando === botao) {
        window.speechSynthesis.cancel();
        finalizarFala();
        return;
    }

    window.speechSynthesis.cancel();
    if (botaoFalando) {
        atualizarBotaoDeFala(botaoFalando, false);
    }

    const textoLimpo = textoParaVoz(texto);
    filaDeFala = textoLimpo.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [textoLimpo];
    filaDeFala = filaDeFala.map(trecho => trecho.trim()).filter(Boolean);
    indiceDaFala = 0;
    botaoFalando = botao;
    atualizarBotaoDeFala(botao, true);

    const iniciar = () => falarProximoTrecho(vozBrasileira(), botao);
    if (window.speechSynthesis.getVoices().length) {
        iniciar();
    } else {
        window.speechSynthesis.onvoiceschanged = iniciar;
    }
}

function ouvirPergunta() {
    const Reconhecimento = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!Reconhecimento) {
        adicionarMensagem("Seu navegador não oferece reconhecimento de voz. Você ainda pode digitar sua pergunta.", "bot");
        return;
    }

    const reconhecimento = new Reconhecimento();
    reconhecimento.lang = "pt-BR";
    reconhecimento.interimResults = false;
    reconhecimento.maxAlternatives = 1;
    reconhecimento.onresult = evento => {
        document.getElementById("mensagem").value = evento.results[0][0].transcript;
        enviar();
    };
    reconhecimento.onerror = () => {
        adicionarMensagem("Não consegui ouvir. Verifique a permissão do microfone e tente novamente.", "bot");
    };
    reconhecimento.start();
}

function registrarFeedback(pergunta, botao) {
    fetch("/feedback", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pergunta: pergunta })
    })
    .then(async response => {
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
            throw new Error(data.erro || "Não foi possível registrar o feedback.");
        }
        return data;
    })
    .then(data => {
        botao.textContent = data.ok ? "Aprendido" : "Obrigado";
        botao.disabled = true;
    })
    .catch(error => console.error("Erro no feedback:", error));
}

// Permitir enviar com Enter
document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("mensagem");
    if ("speechSynthesis" in window) {
        window.speechSynthesis.getVoices();
        window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
    }
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            enviar();
        }
    });
});
