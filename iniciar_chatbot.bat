@echo off
cd /d "%~dp0"
:inicio
"%~dp0.venv\Scripts\python.exe" -u app.py >> "%~dp0servidor.log" 2>&1
timeout /t 2 /nobreak >nul
goto inicio
