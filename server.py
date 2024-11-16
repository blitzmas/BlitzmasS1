# Versiones disponibles
# forge, mohist, fabric, vanilla, paper

# Puedes instalar mohist después de instalar forge desde el menú de gestionar
# Puedes instalar paper después de instalar vanilla desde el menú de gestionar
# Puedes instalar purpur después de instalar fabric desde el menú de gestionar

# Regiones de ngrok
# Código          Lugar
#-----------      ---------------------------
# ap          Asia / Pacífico (Singapore)
# au          Australia (Sydney)
# eu          Europa (Frankfurt)
# in          India (Mumbai)
# jp          Japón (Tokyo)
# sa          Sudamérica (São Paulo)
# us          Estados Unidos (Ohio)
# us-cal-1    Estados Unidos (California)

import requests
import os
import base64
import glob
import time

# Remove "servidor.py" if it exists
if os.path.exists("servidor.py"):
    os.remove("servidor.py")

# Create ".gitignore" if it doesn't exist
if not os.path.exists("./.gitignore"):
    big = (
        "L1B5dGhvbioNCi93b3JrX2FyZWEqDQovc2Vydmlkb3JfbWluZWNyYWZ0DQovbWluZWNyYWZ0X3NlcnZlcg0KL3NlcnZpZG9yX21pbmVjcmFmdF9vbGQNCi90YWlsc2NhbGUtY3MNCi90aGFub3MNCi9zZXJ2ZXJzDQovYmtkaXINCi92ZW5kb3INCmNvbXBvc2VyLioNCmNvbmZpZ3VyYXRpb24uanNvbg0KY29uZmlndXJhY2lvbi5qc29uDQoqLnR4dA0KKi5weWMNCioubXNwDQoqLm91dHB1dA=="
    )
    dec = base64.standard_b64decode(big).decode()
    with open(".gitignore", "w") as giti:
        giti.write(dec)

# Function to download the latest release
def download_latest_release(download_path="."):
    mirror = "https://elyxdev.github.io/latest"
    response = requests.get(mirror)
    if response.status_code == 200:
        data = response.json()
        url = data.get("latest")
        version = url.split("/")[-1]

        # Check if the latest version is already downloaded
        if version in glob.glob("*.msp"):
            return version
        else:
            # Remove any old .msp files
            for old_file in glob.glob("*.msp"):
                os.remove(old_file)

            print("Actualizando tu versión de MSP...")
            time.sleep(1.5)

            # Download the latest version
            path_to_file = os.path.join(download_path, version)
            with open(path_to_file, "wb") as archivo:
                archivo.write(requests.get(url).content)
            return version
    else:
        print("No se pudo conectar al servidor para descargar la última versión.")
        return None

# Download and execute the latest release
flnm = download_latest_release()
if flnm:
    if flnm.split(".")[-1] == "msp":
        os.system(f"chmod +x {flnm} && ./{flnm}")
    else:
        os.system(f"python3 {flnm}")
