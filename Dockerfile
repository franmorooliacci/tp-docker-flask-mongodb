FROM python:3.8-slim

# Instalar Apache y mod_wsgi
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-wsgi-py3 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
RUN pip install flask pymongo

# Copiar el código de la aplicación y la configuración de Apache
COPY ./app /var/www/app
COPY ./myapp.conf /etc/apache2/sites-available/000-default.conf

# Habilitar el módulo wsgi
RUN a2enmod wsgi

EXPOSE 80
CMD ["/bin/bash", "-c", "source /etc/apache2/envvars && exec apache2 -D FOREGROUND"]
