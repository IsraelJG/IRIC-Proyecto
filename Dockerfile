FROM python:3.11-slim
## Materia: Automatizacion de Infraestructura II
## Profesor
## Alumno: Marvin Israel Jaramillo Garcia
WORKDIR /app

# dependencias del sistema para curl (healthcheck) y gcc si se necesita compilar
RUN apt-get update && apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5000
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
