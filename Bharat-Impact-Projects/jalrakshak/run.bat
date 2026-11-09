@echo off
cd /d "%~dp0"
set PORT=8011
start "JalRakshak local server" cmd /k python server.py
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8011
