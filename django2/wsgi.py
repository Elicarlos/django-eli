"""
WSGI config for django2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from typing import ClassVar

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling
# Cling apresenta os arquivos staticos 
# MediaCling apresenta os arquivos de upload

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

application = Cling(MediaCling(get_wsgi_application()))
