# Entrega Proyecto 1
## Guía para desplegar 
1. **Clonar el repositorio en la carpeta desde la que se quiere ejecutar el notebook**
   ```console
   git clone git@github.com:danielj4mv/proyecto_1.git
   ```
2. **Ingresar desde la terminal a la carpeta en que se encuentra el archivo `docker-compose.yaml`**
   ```docker
   cd proyecto_1
   ```
3. **Compilar la aplicación de docker ejecutando el siguiente comando en terminal**

   ```docker
   docker compose build
   ```
   Al ejecutar este comando se descarga una imagen de alrededor de 20 gigas, por lo que puede demorar horas en terminar de ejecutarse, asegurese de contar con el espacio necesario para este proceso.
   
5. **Crear el contenedor de docker ejecutando el siguiente comando en terminal (desde la misma  carpeta)**
   ```docker
   docker compose up
   ```
6. **Una vez se ha terminado de ejecutar el comando anterior, en las últimas líneas se muestra como acceder a la interfaz de jupyterlab expuesta en el puerto 8888. Acceder a cualquiera de los elaces proporcionados desde su navegador de preferencia**
7. **Una vez dentro, desde la interfaz de jupyterlab se pide un token de acceso el cual fue proporcionado junto al enlace. Copiar y pegar este token en el espacio requerido para acceder**
8. **Desde la interfaz en jupyterlab se puede acceder al notebook `proyecto_1.ipynb` con el desarrollo correspondiente al proyecto 1**
