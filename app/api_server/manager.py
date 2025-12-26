import psutil
from app.api_server.minecraft import MinecraftServer
from app.models import Servidor, Configuracao, db

servers = {}


def load_servers_from_db():
    servidores = Servidor.query.all()
    config = Configuracao.query.first()
    if not config:
        config = Configuracao()

    config.ftp_ativo = False

    db.session.add(config)
    db.session.commit()

    for s in servidores:
        servers[s.id] = MinecraftServer(
            server_path=s.path,
            jar="server.jar",
            ram_mb=s.ram * 1024,
            port=s.porta
        )

        # Verificar se estava rodando antes
        if s.pid and psutil.pid_exists(s.pid):
            servers[s.id].pid = s.pid
            servers[s.id].start_time = s.start_time
        else:
            s.status = "parado"
            s.pid = None

def add_server(s):
    servers[s.id] = MinecraftServer(
            server_path=s.path,
            jar="server.jar",
            ram_mb=s.ram * 1024,
            port=s.porta
        )
    
    if s.pid and psutil.pid_exists(s.pid):
            servers[s.id].pid = s.pid
            servers[s.id].start_time = s.start_time
    else:
        s.status = "parado"
        s.pid = None

def start_server(server_id):
    server = servers.get(server_id)
    servidor_db = Servidor.query.get(server_id)

    if not server or server.is_running():
        return False

    server.start()

    servidor_db.pid = server.pid
    servidor_db.status = "rodando"
    servidor_db.start_time = server.start_time
    db.session.commit()

    return True


def stop_server(server_id):
    server = servers.get(server_id)
    servidor_db = Servidor.query.get(server_id)

    if not server or not server.is_running():
        return False

    server.stop()

    servidor_db.pid = None
    servidor_db.status = "parado"
    servidor_db.start_time = None
    db.session.commit()

    return True


def get_status(server_id):
    server = servers.get(server_id)
    if not server:
        return None
    return server.status()

def get_logs(server_id):
    server = servers.get(server_id)
    if not server:
        return []
    return server.logs

def send_command(server_id, cmd):
    server = servers.get(server_id)
    if not server:
        return False
    server.send_command(cmd)
    return True