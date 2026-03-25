@echo off
set BASE=C:\Users\Covert\Dev\File_Log

echo Creating folder structure under %BASE%
echo.

rem --- Core app folders ---
mkdir "%BASE%\app"
mkdir "%BASE%\app\watcher"
mkdir "%BASE%\app\db"
mkdir "%BASE%\app\models"
mkdir "%BASE%\app\utils"
mkdir "%BASE%\app\analytics"
mkdir "%BASE%\app\tui"
mkdir "%BASE%\app\tui\views"

rem --- Tests ---
mkdir "%BASE%\tests"

rem --- Data ---
mkdir "%BASE%\data"
mkdir "%BASE%\data\logs"

rem --- Config ---
mkdir "%BASE%\config"

rem --- Scripts ---
mkdir "%BASE%\scripts"

echo.
echo Folder structure created successfully.
pause