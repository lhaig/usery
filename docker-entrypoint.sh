#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /usery/logs/gunicorn.log
touch /usery/logs/access.log
tail -n 0 -f /usery/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
# exec gunicorn sandbox.wsgi:application --bind 0.0.0.0:8000 --workers 3
exec gunicorn usery.wsgi.application \
    --name usery \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/usery/logs/gunicorn.log \
    --access-logfile=/usery/logs/access.log \
    "$@"
