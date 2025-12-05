#!/bin/bash

# Указать домен
domain="dashkov.ru"


source ./app/venv/bin/activate

python app/main.py "$domain"
