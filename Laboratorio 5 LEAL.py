from virus_total_apis import PublicApi
from datetime import date

#d3 fecha de analisi
today = date.today()
d3 = today.strftime("%d/%m/%Y")
print("Dia de hoy", d3)

f = open("Url.txt","r")
lines = f.readlines()
f.close()
#url
print(lines[1])

API_KEY = "558336c3a4949fe01bb7830f43c3f12af88414012661b3abfb2c80693c0ae2a4"

api = PublicApi(API_KEY)
#Hacer un for que acabe cuando termine de leer las url
response = api.get_url_report(lines[1])

if response["response_code"] == 200:
       #Analisis positivos
       # con un if se hace la clasificacion
       print(response["results"]["positives"])
        #total de analisis
       print(response["results"]["total"])
else:
    print("No ha podido obtenerse el análisis del archivo.")