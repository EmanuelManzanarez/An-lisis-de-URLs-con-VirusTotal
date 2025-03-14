# metadatos-imagenes
Análisis de URLs con VirusTotal
Este script permite analizar URLs utilizando la API de VirusTotal. Extrae las URLs desde un archivo de texto (Url.txt), consulta el estado de la URL en VirusTotal y muestra el número de detecciones positivas y el total de análisis realizados.

Requisitos
Antes de ejecutar el script, asegúrate de cumplir con los siguientes requisitos:

Python 3 instalado.
Módulo virus_total_apis instalado: Puedes instalarlo con:
bash
Copiar
Editar
pip install virus-total-api
Tener una clave API de VirusTotal.
Puedes obtener una clave API gratuita registrándote en VirusTotal.
Uso
Guarda el script en un archivo (analisis_url.py).

Crea un archivo Url.txt en la misma carpeta del script y agrega las URLs que deseas analizar, cada una en una línea diferente.

Ejecuta el script desde la terminal o línea de comandos:

bash
Copiar
Editar
python analisis_url.py
Salida esperada:

Si la URL se ha analizado correctamente, el script mostrará la cantidad de detecciones positivas y el total de análisis.
Si ocurre un error, mostrará un mensaje indicando que no se pudo obtener el análisis.
