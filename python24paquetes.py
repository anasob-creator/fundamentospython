###########    PAQUETES. ###############
# # Un paquete es un conjunto de librerías que podemos utilizar en múltiples equipos
# SI NO TENEMOS NUESTRO fichero de librerías no podemos utilizarlo en casa
# Existe la posibilidad de hacer un package de Python con nuestras librerías
# Pero el problema es que si no tengo ese paquete accesible no tengo las librerías para poder trabajar
# Existe un repositorio de librerías para todo python
# En dicho repositorio están todos los tipos de librerías que se nos ocurran, desde web scraping o lo que sea
# Cualquiera puede subir sus paquetes, publicarlos y acceder a ellos desde cualquier lugar.
# Para instalar estas librerías necesitamos la 3.11 o sup. 
# Para poder utilizar estas librerías necesitamos un comando llamado pip
#PIP# nos permite agregar todas las librerías de paquetes a nuestro equipo
# tenemos la pág. web accesible
# https://pypi.org
# el comando para instalar librerías es:
# pip install nombre de librería
# En el SO macOS se utliizar pip3
# vamos a crear un instalador de nuestra aplicación de forma que lo podremos ejecutar
# sin tener necesidad de tener python, ni compilador ni VScode
# En Windows, esto nos genera un .exe, en Mac un .pkg
# NOTA: no importa dónde pongamos el comando de pip install, las librerías se instalan
# a nivel de SO.
# vamos a hacer un ejemplo por terminal
# nos descargamos pip3 install pyinstaller que descarga un ejecutable en el SO.
# para probarlo nos vamos un archivo pyton que no tenga dependencias (sin librerías)
# desde el terminal entramos a nuestra carpeta con el comando
# cd nombreCarpeta, para ver lo que hay ls vemos las carpetas 
# entramos en ellas, con el tab. según escribimos nos autocompleta
# pyinstaller -c -F NOMBREPYTHON    
# Me ha creado una carpeta dist con un ejecutable
