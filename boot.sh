#!/bin/bash
while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retyring in 5 secs...
    sleep 5
done
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - wsgi:app
