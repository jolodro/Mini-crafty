# Endereço e porta
bind = "0.0.0.0:8000"

# Quantidade de workers
workers = 1

# Tipo de worker
worker_class = "sync"

worker_class = "gthread"

# Tempo máximo antes de matar worker travado
timeout = 120

# Logs
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Nome do processo
proc_name = "painel_flask"

# Preload da aplicação (melhora desempenho)
preload_app = True
