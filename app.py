from flask import Flask, render_template, request, jsonify
from chatbot import responder, buscar_versiculo
from ia_gemini import responder_com_ia
from modelo_ml import registrar_aprendizado

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/chat", methods=["POST"])
def chat():
    dados = request.get_json(silent=True)
    mensagem = dados.get("mensagem", "").strip() if isinstance(dados, dict) else ""
    if not mensagem:
        return jsonify({"erro": "Digite uma pergunta para continuar."}), 400

    # Tentar buscar versículo na API (ex: "João 3:16")
    resultado_versiculo = buscar_versiculo(mensagem)
    
    if resultado_versiculo:
        resposta = resultado_versiculo
    else:
        resposta = responder_com_ia(mensagem) or responder(mensagem)

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