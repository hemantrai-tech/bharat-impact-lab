@echo off
cd /d "%~dp0"
set PORT=8013
start "KisanSetu local server" cmd /k python server.py
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8013
