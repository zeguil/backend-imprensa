#!/usr/bin/env bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn memorial.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 1 \
    --chdir  memorial-backend
