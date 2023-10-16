@echo off
:loop
FOR /F "tokens=*" %%i IN ('docker ps -q --filter  "ancestor=clp"') DO SET container_id=%%i
IF NOT "%container_id%"=="" (
    docker cp %container_id%:/resultados resultados
)
timeout /t 1 > NUL
goto loop
