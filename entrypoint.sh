#!/bin/bash
python manage.py create_db
exec "$@"
