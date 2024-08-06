@echo off
title Aqua
color B
mode 120,80
:inicio
echo.
echo  -------------------------------
echo  -
echo  = 	       MENU	       =
echo  -
echo  -------------------------------
echo.
echo.
echo  ::
echo  ::    1-Reddit.com
echo  ::    2-Buscar en Reddit
echo  ::    3-Youtube
echo  ::    4-Buscar en Youtube
echo  ::    5-Mover modsM
echo  ::    6-Salir
echo  ::     
echo.
set /p menu=opcion=

if "%menu%"=="1" goto op1

if "%menu%"=="2" goto op2

if "%menu%"=="3" goto op3

if "%menu%"=="4" goto op4

if "%menu%"=="5" goto op5

if "%menu%"=="6" goto salir

if "%menu%"=="7" goto op7

else echo Esa opción no existe

:op1 
cls
start https://www.reddit.com
cls
echo Apretar cualquier letra...
pause>nul
cls
goto inicio

:op2
cls
echo.
set /p buscar=Busqueda=
echo.
start https://www.reddit.com/search/?q=%buscar%
cls
echo Apretar cualquier tecla...
pause>nul
cls
goto inicio

:op3
cls
echo.
start www.youtube.com
cls
echo Apretar cualquier letra...
pause>nul
cls
goto inicio

:op4
cls
echo.
set /p buscaryt=Busqueda=
set /p buscarytb=Busqueda2daL=
echo.
start https://www.youtube.com/results?search_query=%buscaryt%+%buscarytb%
cls
echo Apretar cualquier letra...
pause>nul
cls
goto inicio

:op5
cls
set /p link=Direccion=
set /p name=Nombre=
XCopy %link% C:\Users\%name%\AppData\Roaming\.minecraft /s
cls
echo Apretar cualquier letra...
pause>nul
cls
goto inicio

:op7
cd (path)
python Calculadora.py
pause>nul
cls
goto inicio

:salir
cls&exit
