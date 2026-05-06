FROM mcr.microsoft.com/devcontainers/python:3.11

# Evita que Python genere archivos .pyc innecesarios
ENV PYTHONDONTWRITEBYTECODE 1
# Permite que los logs lleguen a la terminal en tiempo real
ENV PYTHONUNBUFFERED 1

WORKDIR /workspaces/mi-agente-pandas

# Instalamos las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# El comando COPY . . no es necesario en Codespaces porque 
# él monta automáticamente tu código como un volumen.
