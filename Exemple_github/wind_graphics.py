# Pràctica 3 Exercici 2
# Adrià Seseras i Víctor Pérez

import matplotlib.pyplot as plt
import pandas as pd

# 1. Lectura de dades de fitxer csv

df = pd.read_csv('nc2csv.csv')                             # Guardem l'arxiu de format csv en una variable "df"

# 2. Extreure les dades de data_time, wind_speed i wind_method amb la llibreria pandas, i convertir dates a bon format

df['date_time'] = pd.to_datetime(df['date_time'])         # Canviem la columna "date_time" a format de dates i hores

date_time = df["date_time"]                               # Agafem la variable 'date_time' del csv i la guardem a una variable "date_time"
wind_speed = df["wind_speed"]                             # Agafem la variable 'wind_speed' del csv i la guardem a una variable "wind_speed"
wind_method = df["wind_method"]                           # Agafem la variable 'wind_method' del csv i la guardem a una variable "wind_method"

# 3. Generar histograma amb les dades de velocitat del vent

plt.hist(wind_speed, color='b')
plt.xlabel('Velocitat del vent')
plt.ylabel('Frequència')
plt.title('Histograma de la velocitat del vent')
plt.show()

# 4. Generar gràfica amb les dades de temps al eix x, les dades de velocitat del vent al eix y, quan wind_method es delayed-mode

wind_method_D = df[df["wind_method"] == "b'D'"]     # Guardem a la variable "wind_method_D" les files on "wind_method" és 1
date_time1 = wind_method_D['date_time']             # Guardem a la variable "date_time1" el "data_time" de les files filtrades per "wind_method_D"
wind_speed1 = wind_method_D['wind_speed']           # Guardem a la variable "wind_speed1" el "wind_speed" de les files filtrades per "wind_method_D"

plt.plot(date_time1, wind_speed1, color='r', linestyle='-', marker='*')
plt.xticks(rotation=45)
plt.xlabel('Temps')
plt.ylabel('Velocitat vent')
plt.title('Velocitat del vent al llarg del temps (Delayed-mode)')
plt.show()

# 5. Generar gràfica amb les dades de temps al eix x, les dades de velocitat del vent al eix y, quan wind_method es real-time

wind_method_R = df[df["wind_method"] == "b'R'"]           # Guardem a la variable "wind_method_R" les files on "wind_method" és 2
date_time2 = wind_method_R['date_time']                   # Guardem a la variable "date_time2" el "data_time" de les files filtrades per "wind_method_R"
wind_speed2 = wind_method_R['wind_speed']                 # Guardem a la variable "wind_speed2" el "wind_speed" de les files filtrades per "wind_method_R"

plt.plot(date_time2, wind_speed2, color='b', linestyle='-', marker='o')
plt.xticks(rotation=45)
plt.xlabel('Temps')
plt.ylabel('Velocitat vent')
plt.title('Velocitat del vent al llarg del temps (Real-time)')
plt.show()