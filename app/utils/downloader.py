import requests
import os

MANIFEST_URL = "https://piston-meta.mojang.com/mc/game/version_manifest.json"

def baixar_servidor_java(versao, pasta):
    manifest = requests.get(MANIFEST_URL).json()

    versao_info = next(v for v in manifest["versions"] if v["id"] == versao)
    version_data = requests.get(versao_info["url"]).json()

    server_url = version_data["downloads"]["server"]["url"]

    destino = os.path.join(pasta, "server.jar")
    with open(destino, "wb") as f:
        f.write(requests.get(server_url).content)

    return destino

def baixar_servidor_bedrock(url_zip, pasta):
    import zipfile, io

    response = requests.get(url_zip)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        zip_ref.extractall(pasta)
