#!/bin/bash
# Активируем виртуальную среду
source venv/bin/activate
# Устанавливаем зависимости
pip install -r requirements.txt
# Запускаем приложение
python app.py &
