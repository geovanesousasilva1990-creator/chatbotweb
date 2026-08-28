@echo off
netsh advfirewall firewall delete rule name="ChatBotWeb Flask 5000" >nul 2>&1
netsh advfirewall firewall add rule name="ChatBotWeb Flask 5000" dir=in action=allow protocol=TCP localport=5000 profile=private
if errorlevel 1 (
  echo ERRO: clique com o botao direito e escolha "Executar como administrador".
) else (
  echo Porta 5000 liberada na rede local.
)
pause
