FROM python:3.12-slim

WORKDIR /app

# Copia os requisitos específicos do microsserviço
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte do microsserviço correspondente
COPY . .

# Usamos a variável de ambiente PORT (definida no docker-compose)
# Caso não esteja definida, o padrão será a porta informada no CMD
EXPOSE $PORT

# Inicializa o Flask lendo a porta correta dinamicamente
CMD ["sh", "-c", "python -u run.py --port=${PORT}"]