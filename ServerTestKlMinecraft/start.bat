@ECHO OFF
cd /d "%~dp0"
"C:\Program Files\Java\jdk-21\bin\java.exe" -Xms1024M -Xmx1024M -jar server.jar
pause