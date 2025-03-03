@echo off
chcp 65001 >nul
@title KLTOOL - by kltzqu / kltz4074
@color 9



echo.
echo		██╗  ██╗██╗  ████████╗ ██████╗  ██████╗ ██╗     
echo		██║ ██╔╝██║  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
echo		█████╔╝ ██║     ██║   ██║   ██║██║   ██║██║     
echo		██╔═██╗ ██║     ██║   ██║   ██║██║   ██║██║     
echo		██║  ██╗███████╗██║   ╚██████╔╝╚██████╔╝███████╗
echo		╚═╝  ╚═╝╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚══════╝            
echo.
echo.
echo. 		
echo      	 (1) start tool



set /p input="⠀⠀⠀⠀⠀⠀⠀⠀>>"

if "%input%"=="1" (
    python files\main.py
)

if "%input%"=="2" (
    start downloadPython.bat
)
pause
