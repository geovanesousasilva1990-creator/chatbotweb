# 🎯 RESUMO RÁPIDO - DEPLOY EM 3 PASSOS

## Seu chatbot está pronto! ✅

Agora precisa apenas colocá-lo online. Siga os 3 passos abaixo:

---

## 📥 PASSO 1: Instale Git (5 minutos)

```
Baixe em: https://git-scm.com/download/win
Execute o instalador
Deixe as opções padrão
Reinicie o terminal
```

---

## 📤 PASSO 2: Envie para GitHub (10 minutos)

### A) Crie repositório vazio no GitHub
```
1. Acesse: https://github.com/new
2. Nome: chatbot-web
3. Descrição: Chatbot bíblico
4. Clique em "Create repository"
5. Copie a URL (https://github.com/SEU_USERNAME/chatbot-web.git)
```

### B) Execute o script de deploy
```
1. Abra a pasta: C:\Users\geova\OneDrive\Área de Trabalho\ChatBotWeb
2. Clique 2x em: deploy_github.bat
3. Cole a URL do GitHub
4. Pronto! ✅
```

---

## 🌐 PASSO 3: Configure no Render (5 minutos)

```
1. Acesse: https://render.com
2. Login com GitHub
3. Clique "New" → "Web Service"
4. Selecione seu repositório chatbot-web
5. Build Command: pip install -r requirements.txt
6. Start Command: gunicorn app:app
7. Plan: Free (gratuito)
8. Clique "Create Web Service"
9. Aguarde 2-3 minutos ⏳
10. Você receberá uma URL! 🎉
```

---

## ⏰ MANTER SERVIDOR 24/7

Render hiberna após 15 min. Para manter acordado:

```
1. Acesse: https://uptimerobot.com
2. Crie conta
3. "Add New Monitor"
4. URL: sua URL do Render
5. Intervalo: 5 minutos
6. Pronto! 24/7 acordado ✅
```

---

## 🎊 RESULTADO FINAL

✅ Chatbot online 24/7  
✅ URL: `https://seu-app.onrender.com`  
✅ Acesso de qualquer lugar  
✅ Totalmente gratuito  

---

## 📞 Precisa de Ajuda?

Abra: `DEPLOY_PASSO_A_PASSO.md` para instruções detalhadas

---

**Tempo total: ~20 minutos** ⏱️
