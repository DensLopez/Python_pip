#Indicar desde que version de Python va a
#partir este ambiente, creando un contenedor
FROM python:3.9
#creando una carpeta dentro del contenedor
WORKDIR /app
#Copiar archivo de dependencias
#Formato: Fuente - Destino(Contenedor)
COPY requirements.txt /app/requirements.txt
#Dejar listo e instalar dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#Copiar nuestro codigo
COPY . /app
#Comando para que el contenedor este corriendo continuamente
#mediante uvicorn para mantener prendido el servidor
#Va correr en el puerto 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]