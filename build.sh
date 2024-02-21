#!/bin/bash


# Install packages
pip install -r requirements.txt

# Upgrade pip
python -m pip install --upgrade pip

# Collect static files
python manage.py collectstatic --noinput
