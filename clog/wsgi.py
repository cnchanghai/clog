"""
WSGI config for clog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
#sys.path.append('/usr/local/lib64/python3.6/site-packages')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clog.settings")
from django.core.wsgi import get_wsgi_application
from os.path import join,dirname,abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))#3
sys.path.insert(0,PROJECT_DIR) # 5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clog.settings")
application = get_wsgi_application()
