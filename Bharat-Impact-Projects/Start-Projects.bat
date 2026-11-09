@echo off
setlocal
start "JalRakshak" /min /D "%~dp0jalrakshak" cmd /c "set PORT=8011&& python server.py"
start "SaansMap" /min /D "%~dp0saansmap" cmd /c "set PORT=8012&& python server.py"
start "KisanSetu" /min /D "%~dp0kisansetu" cmd /c "set PORT=8013&& python server.py"
start "SeekhoSaath" /min /D "%~dp0seekhosaath" cmd /c "set PORT=8014&& python server.py"
start "SwasthyaSetu" /min /D "%~dp0swasthyasetu" cmd /c "set PORT=8015&& python server.py"
start "KaamNirmaan" /min /D "%~dp0kaamnirmaan" cmd /c "set PORT=8016&& python server.py"
start "SurakshaSaathi" /min /D "%~dp0surakshasaathi" cmd /c "set PORT=8017&& python server.py"
start "SwachhChain" /min /D "%~dp0swachhchain" cmd /c "set PORT=8018&& python server.py"
start "HaqSaathi" /min /D "%~dp0haqsaathi" cmd /c "set PORT=8019&& python server.py"
timeout /t 3 /nobreak >nul
start "" "%~dp0index.html"
echo Bharat Impact Projects is ready. Close the opened server windows to stop the apps.
