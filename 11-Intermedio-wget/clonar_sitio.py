#!/usr/bin/env python3
# Script para clonar sitios web usando wget

import subprocess
import urllib.request

def verificar_wget():
    """Verifica si wget esta disponible"""
    try:
        result = subprocess.run(['wget', '--version'], 
                              capture_output=True, 
                              text=True, 
                              shell=True)
        return result.returncode == 0
    except:
        return False

def instalar_wget():
    """Descarga wget.exe para Windows"""
    wget_url = "https://eternallybored.org/misc/wget/1.21.4/64/wget.exe"
    print("Descargando wget.exe...")
    urllib.request.urlretrieve(wget_url, "wget.exe")
    print("wget.exe descargado correctamente")

def clonar_sitio(url):
    """Clona el sitio web usando wget"""
    
    # Comando wget para Windows
    comando = ' '.join([
        'wget.exe',
        '--mirror',                # Modo espejo (descarga recursiva)
        '--convert-links',         # Convertir enlaces para uso local
        '--adjust-extension',      # Agregar extensiones apropiadas
        '--page-requisites',       # Descargar CSS, JS, imagenes
        '--no-parent',             # No subir a directorios padre
        '--wait=2',                # Esperar 2 segundos entre peticiones
        '--random-wait',           # Variar tiempo de espera
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"',
        '--no-check-certificate',  # No verificar certificados SSL
        '--tries=3',               # Intentos por archivo
        '--timeout=30',            # Timeout de 30 segundos
        url
    ])
    
    print(f"Clonando: {url}")
    print("Esto puede tomar varios minutos...\n")
    
    try:
        proceso = subprocess.run(comando, shell=True)
        
        if proceso.returncode == 0:
            print("\nClonado completado exitosamente")
        else:
            print("\nProceso terminado con advertencias")
            
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario")
    except Exception as e:
        print(f"\nError: {e}")

def main():
    # URL del sitio a clonar
    url = "https://tu.sitio.com.pe/"
    
    # Verificar wget
    if not verificar_wget():
        respuesta = input("wget no encontrado. Descargar? (s/n): ")
        if respuesta.lower() in ['s', 'si', 'y', 'yes']:
            instalar_wget()
        else:
            print("wget es necesario para continuar")
            return
    
    # Clonar sitio
    clonar_sitio(url)

if __name__ == "__main__":
    main()
