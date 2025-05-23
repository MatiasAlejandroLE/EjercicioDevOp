import os
import subprocess

def deploy():
    print("Obteniendo el código del repositorio Git...")
    subprocess.run(["git", "pull"], check=True)
    print("Ejecutando pruebas (si existen)...")
    # Aquí irían las pruebas unitarias, si las tuvieras
    print("Creando el paquete de la aplicación...")
    # Aquí iría la lógica para crear un paquete (ej: zip, tar)
    print("Desplegando la aplicación...")
    # Simula el despliegue copiando el archivo a un directorio de destino
    os.makedirs("destino", exist_ok=True)
    subprocess.run(["cp", "index.html", "destino/index.html"], check=True)
    print("Despliegue completado en la carpeta 'destino'")

if __name__ == "__main__":
    deploy()
