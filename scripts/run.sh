#!/bin/sh
set -e

gunicorn -b :8000 --chdir /app app.wsgi:application