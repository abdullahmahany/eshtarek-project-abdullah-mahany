#!/bin/sh

# Wait for Postgres to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Apply migrations
python manage.py migrate

# Run the server
exec "$@"
