# Imagen base
FROM python:3.10

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
