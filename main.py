
from flask import Flask, render_template
import csv


def leer_markers_desde_csv(ruta_csv="Dipola.csv"):
   markers = []

    
   with open(ruta_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                
                lon_str = row["longitud"].replace(",", ".").strip().strip('"')
                lat_str = row["Latitud"].replace(",", ".").strip().strip('"')

                lon = float(lon_str)
                lat = float(lat_str)
            except (KeyError, ValueError) as e:
                
                print("Fila saltada por error en coordenadas:", e, row)
                continue

            nombre_dep = row["Nombre Departamento"].title()
            nombre_mun = row["Nombre Municipio"].title()

            popup = f"{nombre_mun} ({nombre_dep})"

            markers.append({
                "lat": lat,
                "lon": lon,
                "popup": popup
            })

   return markers



app=Flask(__name__)
@app.route('/')
def root():
   markers= leer_markers_desde_csv("Dipola.csv")
   return render_template('index.html',markers=markers )

if __name__ == '__main__':
   app.run(host="localhost", port=8080, debug=True)