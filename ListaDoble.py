import os

class ListaDoble():
    def __init__(self):
        self.inicio=None

    def report(self):
            ##aux=self.inicio
            text=""
            text+="rankdir=LR; \n "
            text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];"
            text+="labelloc=\"t; \"label = \"Pacientes\";\n"

    def crearReporte(self):
        contenido="digraph G{\n\n"
        r=open("reporte.txt","w")
        contenido+=str(self.report())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("done")
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
        os.system("dot -Tpng reporte.txt -o reporte.png")

