#!/bin/bash

cd /app/learn
echo "Making Django migrations..."
python manage.py makemigrations
python manage.py migrate
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000