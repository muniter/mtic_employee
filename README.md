# Plataforma de Empleados

Misión TIC Grupo 33 Equipo 9

- Raúl López (@galoryzen)
- Javier López (@muniter)
- Hember Garzón 
- Luis Bateman 
- Álvaro Rodríguez (@coarf20)

Tutor: Randy Consuegra (@rsconsuegra)

## Instrucciones de uso

Nota: **El makefile functiona en Linux solamente**, `make all` en pocas palabras corre flask con las variables de entorno correctas `FLASK_ENV=development FLASK_APP=app flask run`, inicializa la base de datos, la llena con test data, y empieza la aplicación.

Navergar a `http://localhost:5000/`

## Deployment

### Cualquier cloud server

En el folder deploy se encuentra un `docker-compose.yaml` que realiza el deployment completo de la app detrás de traefik como reverse proxy, generando los certificados ssl y proveyendo https automáticamente. Solamente es necesario crear el archivo `~/deploy/.env` como el ejemplo provisto en `deploy/.env-example` y correr `docker-compose -f deploy/docker-compose.yaml --env-file deploy/.env up -d` y crear una entrada dns a la ip del servidor (TODO: automate the entry soon).

### Heroku

Build y publish el contenedor `ln -s deploy/Dockerfile ./ && heroku container:push web` luego correlo `heroku container:release web`
