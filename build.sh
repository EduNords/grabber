#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python grabber/manage.py collectstatic --no-input
python grabber/manage.py migrate