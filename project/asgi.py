import os
from decouple import config
from django.core.asgi import get_asgi_application



if config('ENVIRONMENT') == 'PROD':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.development')

application = get_asgi_application()
