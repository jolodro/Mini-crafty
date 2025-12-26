from mcstatus import JavaServer

def ping_java(host="127.0.0.1", port=25565):
    try:
        server = JavaServer(host, port)
        status = server.status()
        return {
            "online": True,
            "players": status.players.online,
            "max_players": status.players.max,
            "motd": status.description
        }
    except:
        return {"online": False}

print(ping_java())