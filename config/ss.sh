#!/bin/bash

set -e

cd /app/learn
echo "Making Django migrations..."
python manage.py makemigrations
python manage.py migrate

# echo "creating superuser..."
# python manage.py createsuperuser --no-input || echo "superuser already exists"

echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000