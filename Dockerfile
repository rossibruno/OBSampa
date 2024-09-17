# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos requirements.txt e instale as dependências
COPY api_observasampa/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o diretório de trabalho
COPY . .

# Exponha a porta 8000
EXPOSE 8000

# Comando para rodar o aplicativo FastAPI com Uvicorn
CMD ["uvicorn", "api_observasampa.main:app", "--host", "0.0.0.0", "--port", "8000"]
