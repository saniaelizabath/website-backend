#!/bin/bash
cd /var/www/magmarine/backend
source venv/bin/activate
source .env
exec uvicorn main:app --host 0.0.0.0 --port 8000
