FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-wsgi-py3 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install flask pymongo

COPY ./app /var/www/app
COPY ./myapp.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod wsgi

EXPOSE 80
CMD ["/bin/bash", "-c", "source /etc/apache2/envvars && exec apache2 -D FOREGROUND"]
