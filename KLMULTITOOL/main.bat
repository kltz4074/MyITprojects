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
echo      	 (1) SIGMA HolyMolyVIDEO
echo     	 (2) start mineraft
echo      	 (3) rutracker
echo          (4) Download MineWays



set /p input="⠀⠀⠀⠀⠀⠀⠀⠀>>"

if "%input%"=="1" (
    start files\videos\video1.mp4
	@start main.bat
)

if "%input%"=="2" (
	start files\Minecraft.exe
	@start main.bat
)

if "%input%"=="3" (
	start files\rutracker.exe
	@start main.bat
)

if "%input%"=="4" (
	start files\DownloadMineways.exe
	@start main.bat
)

if "%input%"=="5" (
	for /l %%x in (1, 1, 10) do start cmd /k "color 2
	
)

if "%input%"=="1488" (
	echo      	 ty dibil?
)

pause
