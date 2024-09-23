# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:34:08 2024

@author: oscar
"""

import requests, sys, json
import pandas as pd

WEBSITE_API = "https://rest.uniprot.org/uniprotkb/stream?format=json&query=%28%28SPATA7+OR+IFT140%29%2BAND%2Bhuman%29"
#query = "SPATA7+AND+human"
#formato = "&format=json"

def get_url(url, **kwargs):
    
    response = requests.get(url, **kwargs)
    
    
    if not response.ok:
        print(response.text)
        response.raise_for_status()
        sys.exit()
        
        
    return response

r=get_url(WEBSITE_API)
datos = r.json()

archivo = {}
numeros_acceso = []
nombres_proteinas = []
funciones = []

archivo["Número de acceso"] = numeros_acceso
archivo["Nombre de proteína"] = nombres_proteinas
archivo["Función"] = funciones


for dato in datos["results"]:
    numeros_acceso.append(dato["primaryAccession"])
    
    if("recommendedName" in dato["proteinDescription"].keys()):
        nombres_proteinas.append(dato["proteinDescription"]["recommendedName"]["fullName"]["value"])
    else:
        nombres_proteinas.append("-")
    
    if("comments" in dato.keys()):
        
        if("texts" in dato["comments"][0].keys()):
            
            funciones.append(dato["comments"][0]["texts"][0]["value"])
            
        else:
            funciones.append("-")
    else:
        funciones.append("-")

# número de acceso: datos["results"][0]["primaryAccession"]
# nombre proteína: datos["results"][0]["proteinDescription"]["recommendedName"]["fullName"]["value"]
# función: datos["results"][0]["comments"][0]["texts"][0]["value"]

df = pd.DataFrame(archivo)
nombre_archivo = "resultados_API.xlsx"
df.to_excel(nombre_archivo)

