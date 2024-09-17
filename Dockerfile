# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Instale as dependências necessárias para o psycopg2-binary
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt da pasta api_observasampa para o diretório de trabalho
COPY api_observasampa/requirements.txt requirements.txt

# Atualize o pip
RUN pip install --upgrade pip

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da pasta api_observasampa
COPY api_observasampa/ /app

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar o aplicativo FastAPI com Uvicorn
CMD ["uvicorn", "api_observasampa.main:app", "--host", "0.0.0.0", "--port", "8000"]
