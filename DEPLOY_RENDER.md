# 🚀 Como Colocar Seu Chatbot Online (Gratuito) - Render.com

## Passo 1: Preparar o Repositório GitHub

1. Crie uma conta em [github.com](https://github.com) (se não tiver)
2. Crie um novo repositório chamado `chatbot-web`
3. Clone para seu computador e copie seus arquivos:
   ```
   app.py
   chatbot.py
   Procfile
   requirements.txt
   static/
   templates/
   ```
4. Faça o commit e push:
   ```
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

## Passo 2: Configurar no Render.com

1. Acesse [render.com](https://render.com) e crie uma conta (com GitHub é mais fácil)
2. Clique em **"New +"** → **"Web Service"**
3. Selecione seu repositório `chatbot-web`
4. Configure:
   - **Name**: `chatbot-web` (ou outro nome)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Escolha o plano Free
   - Em **Environment → Environment Variables**, adicione `GEMINI_API_KEY` com a sua chave do Google Gemini.
   - Se o banco PostgreSQL foi criado separadamente, adicione também `DATABASE_URL` usando a **Internal Database URL** do banco.
5. Clique em **"Create Web Service"**

Se você usar o `render.yaml` como Blueprint, o `DATABASE_URL` será associado automaticamente ao banco `chatbotdb`. O app usa PostgreSQL no Render e continua usando o SQLite/JSON localmente quando essa variável não existe.

## Passo 3: Aguardar o Deploy

- Aguarde 2-3 minutos enquanto o Render faz o deploy
- Você receberá uma URL como: `https://chatbot-web.onrender.com`
- Pronto! Seu chatbot está online 24/7 (com tier free)

## ⚠️ Observações Importantes

- **Tier Free do Render**: O servidor hiberna após 15 min sem atividade
- Solução: Mantenha a aba aberta ou use um serviço como [UptimeRobot](https://uptimerobot.com) (gratuito) para "acordar" o servidor a cada 5 min
- Para usar UptimeRobot: adicione seu URL e defina para fazer ping a cada 5 minutos

## Alternativas Gratuitas

| Plataforma | Vantagens | Desvantagens |
|-----------|-----------|-------------|
| **Render** | Fácil, suporta Python | Hiberna |
| **Railway** | Crédito inicial | Precisa cartão de crédito |
| **PythonAnywhere** | Sempre online (tier free) | Limitado a 2 apps |
| **Replit** | Simples demais | Lento para produção |

