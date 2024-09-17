from core.utils.utils import build_conn_str
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Função para verificar se todas as variáveis de ambiente estão definidas
def check_env_vars():
    required_vars = ['PGHOST', 'PGPORT', 'PGDATABASE', 'PGUSER', 'PGPASSWORD', 'REQUEST_TIMEOUT_ERROR']
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variável de ambiente '{var}' não está definida. Verifique seu arquivo .env.")

# Verifica se todas as variáveis de ambiente necessárias estão presentes
check_env_vars()

# Dados do banco de dados
db_data = {
    'host': os.environ['PGHOST'],  # Adaptar para usar PGHOST
    'port': os.environ['PGPORT'],
    'database': os.environ['PGDATABASE'],
    'user': os.environ['PGUSER'],
    'password': os.environ['PGPASSWORD']
}


# Construa a URL do SQLAlchemy com base nos dados do banco
SQLALCHEMY_DATABASE_URL = build_conn_str(**db_data)

# Valor do tempo limite da requisição
REQUEST_TIMEOUT_ERROR = int(os.getenv('REQUEST_TIMEOUT_ERROR', 500))  # Define 500 como valor padrão se não for encontrado
