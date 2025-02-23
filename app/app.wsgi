import sys
# Agrega la ruta donde pip instala los paquetes
sys.path.insert(0, '/usr/local/lib/python3.8/site-packages')
# Agrega la ruta de la aplicación
sys.path.insert(0, '/var/www/app')
from app import app as application
