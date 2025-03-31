# Usa una imagen ligera de Python
FROM python:3.8-slim

# Crea el directorio de trabajo
WORKDIR /app

# Copia e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu proyecto
COPY . .

# Expone el puerto que usa Flask (puedes cambiarlo si usas otro)
EXPOSE 5000

# Comando para correr la app Flask
CMD ["python", "app.py"]
