@echo off
chcp 65001 > nul
cd /d "Z:\wiki"
if errorlevel 1 goto ERR

echo Knowledge Wiki AGY (Working Dir: Z:\wiki)
echo.
agy %*
goto END

:ERR
echo [ERROR] Cannot change directory to Z:\wiki.
pause
exit /b 1

:END
