


REM Скрипт не работает.
@echo off
set domain=dashkov.ru

REM Активируем виртуальное окружение
call app\venv\Scripts\activate.bat

REM Запускаем Python-скрипт
python app\main.py %domain%

REM Пауза (если нужна)
pause
