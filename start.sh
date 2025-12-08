#!/bin/bash

# Указать домен
#####
domain="dashkov.ru"
#####





source ./app/venv/Scripts/activate

python app/main.py "$domain"