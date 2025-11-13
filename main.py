from flask import Flask, render_template
import csv

from LinkedList import LinkedList
from Node import Node

app = Flask(__name__)
def construir_multilista_desde_csv(ruta_csv="Dipola.csv"):
    paises = LinkedList()

    # Pais raiz: Colombia
    colombia = Node("CO", "Colombia")
    paises.append(colombia)

    with open(ruta_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            dep_code = row["Código Departamento"]
            dep_name = row["Nombre Departamento"].title()
            mun_code = row["Código Municipio"]
            mun_name = row["Nombre Municipio"].title()

            try:
                lon = float(row["longitud"].replace(",", "."))
                lat = float(row["Latitud"].replace(",", "."))
            except:
                continue

           
            if colombia.sub_list is None:
                colombia.sub_list = LinkedList()

            dep_list = colombia.sub_list
            dep_node = dep_list.search_by_attr("id", dep_code)

            if dep_node is None:
                dep_node = Node(dep_code, dep_name)
                dep_list.append(dep_node)

          
            if dep_node.sub_list is None:
                dep_node.sub_list = LinkedList()

            mun_node = Node(mun_code, mun_name)
            mun_node.lat = lat
            mun_node.lon = lon

            dep_node.sub_list.append(mun_node)

    return paises


def multilista_a_markers(paises: LinkedList):
    markers = []

    country = paises.head
    while country:
        dep_list = country.sub_list
        if dep_list:
            dep = dep_list.head
            while dep:
                mun_list = dep.sub_list
                if mun_list:
                    mun = mun_list.head
                    while mun:
                        if mun.lat is not None and mun.lon is not None:
                            markers.append({
                                "lat": mun.lat,
                                "lon": mun.lon,
                                "popup": f"{mun.name} ({dep.name})"
                            })
                        mun = mun.next
                dep = dep.next

        country = country.next

    return markers

PAISES = construir_multilista_desde_csv("Dipola.csv")

@app.route("/")
def root():
    markers = multilista_a_markers(PAISES)
    return render_template("index.html", markers=markers)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)



