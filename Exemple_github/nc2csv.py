# Pràctica 3 Exercici 1
# Adrià Seseras i Víctor Pérez

import netCDF4 as nc
import pandas as pd
import csv
from netCDF4 import num2date

# 1. Lectura de fitxer netCDF

ds = nc.Dataset('wind_data.nc')             # Guardem l'arxiu de format netCDF en una variable "ds"

# 2. i 3. Extreure camps temps, velocitat del vent, mètode de vent, qualitat velocitat de vent

times = ds.variables['time']                # Agafem la variable 'times' de la nostra base de dades ("ds")
wind = ds.variables['WSPD'][:]              # Agafem la variable 'wind' de la nostra base de dades ("ds")
wind_qc =  ds.variables['WSPD_QC'][:]       # Agafem la variable 'wind_qc' de la nostra base de dades ("ds")
wind_method =  ds.variables['WSPD_DM'][:]   # Agafem la variable 'wind_method' de la nostra base de dades ("ds")

# 4. Generar una capçalera

header = ['date_time', 'wind_speed','wind_qc', 'wind_method']

# 5. Extreure les files on la qualitat de la velocitatdel vent sigui 1 i escriure-ho a un fixer csv

dates = num2date(times[:], times.units)     # Pasa les unitats de 'times' de valor númeric a una data

with open('nc2csv.csv', 'w', encoding='UTF8', newline='') as f:  # Es crea l'arxiu csv
    writer = csv.writer(f,delimiter=',')                         # La variable "writer" ens crea cadenes/llistes de dades separades entre si per ,
    writer.writerow(header)                                      # Escriu la capçalera creada a dalt de tot del csv
    i = 0
    data = []
    while i < len(wind_qc):                                        # Començem el bucle que volem que pasi per totes les dades
        newrow = [dates[i], wind[i], wind_qc[i], wind_method[i]]   # Crea una fila amb les 4 variables a cada pas del bucle
        if wind_qc[i] == 1:                                        # Es pregunta si la qualitat de la velocitat es igual a 1
            writer.writerow(newrow)                                # Doncs es crea la fila amb les 4 varibales corresponents

        i += 1                                                     # Quan ha comprobat una fila pasa a la següent


