from core.utils.utils import build_conn_str
import os

# Verifica se está em ambiente de desenvolvimento
ENV = os.getenv('ENV', 'DEVELOPMENT')

if ENV == 'DEVELOPMENT':
    from dotenv import load_dotenv
    load_dotenv()

def check_env_vars():
    required_vars = ['PGHOST', 'PGPORT', 'PGDATABASE', 'PGUSER', 'PGPASSWORD', 'REQUEST_TIMEOUT_ERROR']
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variável de ambiente '{var}' não está definida. Verifique suas variáveis de ambiente.")

check_env_vars()

db_data = {
    'host': os.environ['PGHOST'],
    'port': os.environ['PGPORT'],
    'database': os.environ['PGDATABASE'],
    'user': os.environ['PGUSER'],
    'password': os.environ['PGPASSWORD']
}

SQLALCHEMY_DATABASE_URL = build_conn_str(**db_data)

REQUEST_TIMEOUT_ERROR = int(os.getenv('REQUEST_TIMEOUT_ERROR', 500))
