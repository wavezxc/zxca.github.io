# Compatibility file for deployment
# This file imports the main application from server.py
from server import app

# This allows the deployment to use 'server_postgresql:app' while keeping our main code in server.py
__all__ = ['app']