# backend/eshtarek_backend/management/commands/wait_for_db.py
import os
import sys
import time
import psycopg2
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Wait for PostgreSQL to become available'

    def handle(self, *args, **options):
        max_retries = 10
        delay = 5
        
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        
        for i in range(max_retries):
            try:
                conn = psycopg2.connect(
                    dbname=db_name,
                    user=db_user,
                    password=db_password,
                    host=db_host,
                    port=db_port
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS('Database is available!'))
                return
            except psycopg2.OperationalError:
                self.stdout.write(f'Waiting for database... (Attempt {i+1}/{max_retries})')
                time.sleep(delay)
        
        self.stdout.write(self.style.ERROR('Could not connect to database'))
        sys.exit(1)