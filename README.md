# Diagrama del proyecto
```
                +-----------------+
                |    Cliente      |
                +-----------------+
                        │
                        ▼
                +-----------------+
                |   Docker Host   |
                +-----------------+
                        │
          +-------------------------------+
          |     Red interna de Docker     |
          |         (app-network)         |
          +-------------------------------+
             /                        \
            /                          \
+---------------------+      +--------------------------+
| Contenedor de la    |      |  Contenedor de MongoDB   |
| App Flask + Apache  |<---->|        (mongo)           |
|      (webapp)       |      |                          |
+---------------------+      +--------------------------+
                                       │
                                       │
                                       ▼
                          +------------------------+
                          |  Volumen Persistente   |
                          |     (mongo_data)       |
                          +------------------------+
```

## Notas Adicionales
- La comunicación entre contenedores se realiza a través de la red 'app-network', definida en docker-compose.
- Los datos de MongoDB se almacenan en el volumen persistente 'mongo_data', para asegurar que los datos se conserven entre reinicios.

# Despliegue del proyecto

## Requisitos
- Docker
- Docker Compose

## Instrucciones de Despliegue

1. **Clonar el repositorio:**  
   `git clone git@github.com:franmorooliacci/tp-docker-flask-mongodb.git`

2. **Acceder al directorio del proyecto:**  
   `cd tp-docker-flask-mongodb`

3. **Levantar los contenedores:**  
   `docker-compose up --build`

4. **Acceso a la aplicación:**  
   Abrir un navegador y dirigirse a http://localhost:80 para ver la aplicación en funcionamiento.

