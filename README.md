# Entrega Proyecto 1
## Guía para desplegar 
1. **Clonar el repositorio en local**
   ```console
   git clone git@github.com:danielj4mv/proyecto_1.git
   ```
2. **Desde la carpeta en la que se encuentra el `docker-compose.yaml` Compilar la aplicación de docker**
   ```docker
   docker compose build
   ```
3. **Crear el contenedor de docker**
   ```docker
   docker compose up
   ```
4. **Una vez se ha terminado de ejecutar el comando anterior, en las últimas líneas se muestra como acceder a la interfaz de jupyterlab expuesta en el puerto 8888. Acceder a cualquiera de los elaces proporcionados desde el navegador**
5. **Una vez dentro, desde la interfaz de jupyterlab se pide un token de acceso el cual fue proporcionado junto al enlace. Copiar y pegar este token en el espacio requerido para acceder**
5. **Desde la interfaz en jupyterlab se puede acceder al notebook `proyecto_1.ipynb` conm el desarrollo correspondiente al proyecto 1**
