# backend/eshtarek_backend/views.py
from django.http import JsonResponse
from django.db import connection
import psutil

def health_check(request):
    # Database check
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        db_status = "OK"
    except Exception as e:
        db_status = str(e)

    # Disk check
    disk = psutil.disk_usage('/')
    disk_status = "OK" if disk.percent < 90 else "WARNING"

    # Memory check
    mem = psutil.virtual_memory()
    mem_status = "OK" if mem.available > 100 * 1024 * 1024 else "WARNING"

    return JsonResponse({
        "status": "OK",
        "components": {
            "database": db_status,
            "disk": disk_status,
            "memory": mem_status
        }
    })