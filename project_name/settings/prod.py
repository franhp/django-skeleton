"""
Production settings
"""

from common import *
from os import environ

SECRET_KEY = environ.get('SECRET_KEY', SECRET_KEY)