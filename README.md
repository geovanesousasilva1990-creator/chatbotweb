# 🤖 Chatbot Bíblico - Geovane

Um chatbot inteligente especializado em responder perguntas sobre a Bíblia, criado com Flask e Python.

## 🚀 Funcionalidades

- Respostas sobre personagens bíblicos
- Informações sobre livros da Bíblia
- Conceitos cristianos explicados
- Interface simples e intuitiva

## 📋 Requisitos

- Python 3.8+
- Flask
- Gunicorn

## ⚙️ Instalação Local

```bash
# Clone o repositório
git clone <seu-repositorio>
cd chatbot-web

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

Acesse em: http://localhost:5000

## 🌐 Deploy

Seu chatbot está configurado para fazer deploy no Render.com gratuitamente!

Veja as instruções em [DEPLOY_RENDER.md](DEPLOY_RENDER.md)

## 📂 Estrutura

```
chatbot-web/
├── app.py                 # Aplicação principal
├── chatbot.py             # Lógica do chatbot
├── requirements.txt       # Dependências Python
├── Procfile              # Configuração para Render
├── README.md             # Este arquivo
├── static/
│   ├── style.css         # Estilos
│   └── script.js         # JavaScript
└── templates/
    └── index.html        # Página principal
```

## 📝 Licença

Projeto educacional.
