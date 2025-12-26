import os

# Pasta base do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Caminho onde os servidores Minecraft ficarão
PATH_SERVERS = os.path.join(BASE_DIR, "servers")

# Banco de dados
DATABASE_URI = "sqlite:///database.db"

# Outras configs globais
DEFAULT_MC_PORT = 25565
DEFAULT_RAM_GB = 2

# Garantir que a pasta exista ao iniciar
os.makedirs(PATH_SERVERS, exist_ok=True)
