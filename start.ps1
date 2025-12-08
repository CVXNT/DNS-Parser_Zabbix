# powershell

# Указать нужный домен
#####
$domain = 'dashkov.ru'
#####





$venvPath = '.\app\venv\Scripts\Activate.ps1'
. $venvPath

python app\main.py $domain

# Read-Host "Press Enter to exit"
