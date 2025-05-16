# WSGI placeholder
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wallet_api.settings')

application = get_wsgi_application()
startCommand: gunicorn wallet_api.wsgi:application