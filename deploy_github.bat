@echo off
REM Script automatizado para fazer deploy no GitHub
REM Execute este arquivo DEPOIS de instalar Git

echo ====================================
echo ChatBot - Deploy no GitHub
echo ====================================

cd /d "%~dp0"

REM Verificar se Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERRO: Git nao encontrado!
    echo Baixe em: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Inicializar Git
echo.
echo [1/5] Inicializando Git...
git init

REM Adicionar arquivos
echo [2/5] Adicionando arquivos...
git add .

REM Primeiro commit
echo [3/5] Criando primeiro commit...
git commit -m "Initial commit: ChatBot Biblico com Flask"

REM Renomear branch
echo [4/5] Configurando branch main...
git branch -M main

REM Adicionar repositorio remoto
echo.
echo [5/5] Conectando ao GitHub...
set /p GITHUB_URL="Cole sua URL do GitHub (https://github.com/...): "
git remote add origin %GITHUB_URL%

REM Fazer push
echo.
echo Fazendo upload para GitHub...
git push -u origin main

echo.
echo ====================================
echo Sucesso! Seu codigo esta no GitHub
echo ====================================
echo.
echo Proximos passos:
echo 1. Acesse: https://render.com
echo 2. Crie uma Web Service conectando ao GitHub
echo 3. Use: gunicorn app:app
echo.
echo Para mais detalhes, abra: DEPLOY_PASSO_A_PASSO.md
echo.
pause
