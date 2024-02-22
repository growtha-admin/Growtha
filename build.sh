#!/bin/bash


# Install packages
pip install -r requirements.txt

# Upgrade pip
python3 -m pip install --upgrade pip

# Collect static files
python3 manage.py collectstatic --noinput
