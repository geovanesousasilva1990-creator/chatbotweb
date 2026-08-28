# 🚀 GUIA COMPLETO - COLOCAR CHATBOT ONLINE 24/7

## 📋 Pré-requisitos

### 1. Instale Git
- Baixe em: https://git-scm.com/download/win
- Execute o instalador (deixe as opções padrão)
- Reinicie o terminal PowerShell

### 2. Crie uma conta GitHub
- Acesse: https://github.com/signup
- Confirme seu email

### 3. Crie uma conta Render.com
- Acesse: https://render.com
- Crie conta com GitHub (mais fácil)

---

## 🔧 PASSO 1: Configurar Git (após instalar)

Abra o **PowerShell** e execute:

```powershell
git config --global user.name "Seu Nome Aqui"
git config --global user.email "seu.email@gmail.com"
```

---

## 📤 PASSO 2: Fazer Upload para GitHub

### 2.1 Criar repositório no GitHub
1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `chatbot-web`
   - **Description**: "Chatbot bíblico com Flask - Geovane"
   - **Public**: Sim
3. Clique em **"Create repository"**
4. Copie a URL do repositório (começa com `https://github.com/`)

### 2.2 Fazer push do código

Abra **PowerShell** na pasta do projeto:
```
C:\Users\geova\OneDrive\Área de Trabalho\ChatBotWeb
```

Execute estes comandos NA ORDEM:

```powershell
# 1. Inicializar Git
git init

# 2. Adicionar todos os arquivos
git add .

# 3. Criar primeiro commit
git commit -m "Initial commit: ChatBot Bíblico"

# 4. Renomear branch para main
git branch -M main

# 5. Adicionar repositório remoto (COLE SUA URL DO GITHUB AQUI)
git remote add origin https://github.com/SEU_USERNAME/chatbot-web.git

# 6. Fazer push para GitHub
git push -u origin main
```

**Substitua `SEU_USERNAME` pelo seu usuário GitHub!**

---

## 🌐 PASSO 3: Deploy no Render.com

### 3.1 Conectar ao Render
1. Acesse: https://render.com/dashboard
2. Clique em **"New +"** → **"Web Service"**
3. Selecione **"Connect a repository"**
4. Autorize o acesso ao GitHub
5. Selecione `chatbot-web`

### 3.2 Configurar o Deploy
1. Preencha:
   - **Name**: `chatbot-web`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Escolha o **Free** (gratuito)

2. Clique em **"Create Web Service"**

### 3.3 Aguardar Deploy
- Leva 2-3 minutos
- Você receberá uma URL como: `https://chatbot-web.onrender.com`

---

## ⏰ MANTER O SERVIDOR ACORDADO (Importante!)

### Problema do Tier Free:
O Render hiberna seu servidor após 15 minutos de inatividade.

### Solução: Use UptimeRobot (GRATUITO)

1. Acesse: https://uptimerobot.com
2. Crie conta (use email)
3. Clique em **"Add New Monitor"**
4. Preencha:
   - **Monitor Type**: HTTP(s)
   - **URL**: `https://chatbot-web.onrender.com` (sua URL)
   - **Check Interval**: 5 minutos
5. Clique em **"Create Monitor"**

✅ **Agora seu servidor ficará acordado 24/7!**

---

## 📂 Estrutura Esperada

Seus arquivos já estão prontos:

```
ChatBotWeb/
├── app.py                 ✅ (atualizado)
├── chatbot.py             ✅ (atualizado com API)
├── requirements.txt       ✅ (atualizado)
├── Procfile              ✅ (pronto)
├── README.md             ✅
├── .gitignore            ✅
├── .gitattributes        ✅
├── static/
│   ├── script.js         ✅
│   └── style.css         ✅
└── templates/
    └── index.html        ✅
```

---

## ✅ RESUMO RÁPIDO

| Etapa | Ação | Tempo |
|-------|------|-------|
| 1️⃣ Git | Instale e configure | 5 min |
| 2️⃣ GitHub | Crie repo e faça push | 5 min |
| 3️⃣ Render | Configure e faça deploy | 3 min |
| 4️⃣ UptimeRobot | Mantenha servidor acordado | 2 min |
| **Total** | **⏱️ 15 minutos** | **24/7 online!** |

---

## 🔗 Links Úteis

- Git: https://git-scm.com/
- GitHub: https://github.com
- Render: https://render.com
- UptimeRobot: https://uptimerobot.com
- Bible API: https://bible-api.com

---

## 🆘 Precisa de Ajuda?

Se encontrar problemas:
1. Verifique se Git está instalado: `git --version`
2. Teste conexão GitHub: `git clone https://github.com/SEU_USERNAME/chatbot-web.git`
3. Verifique logs no Render.com Dashboard

**Seu chatbot estará online em minutos!** 🚀
