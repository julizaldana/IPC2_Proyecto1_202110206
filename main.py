#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2 - B
#PROYECTO 1

import os
from typing import List
from xml.dom import minidom


def menu():
    print("---------------------------------------------")
    print("MENU INVESTIGACION EPIDEMIOLOGICA DE GUATEMALA")
    print("1. Cargar un archivo")
    print("2. Salir")
    print("---------------------------------------------")
    respuesta = input("Ingrese una opcion: ")

    if respuesta=='1':
        Filename=input('Ingresar nombre de archivo: ')
        file='./'+Filename
        documentoxml = minidom.parse(file)
        pacientes = documentoxml.getElementsByTagName("paciente")
        print("----------------------------------------------------------")
        print("            Lista de Pacientes                 ")
        print("----------------------------------------------------------")
        for paciente in pacientes:                    
            nombre = paciente.getElementsByTagName("nombre")[0]
            edad = paciente.getElementsByTagName("edad")[0]
            print("Nombre: " + str(nombre.firstChild.data) + "    " + "Edad: " + str(edad.firstChild.data))

    elif respuesta=='2':
        exit()


    #def crear_reporte():
       #text = ""
        #text += "digraph G {\n\n edge [fontname=\"Helvetica,Arial,san-serif\"]\n"
        #text +="\"pacientes: "+ nombre +"\"\n\n}"
        #nombrearchivo = "reporte_Pacientes"
        #f = open(nombrearchivo+".txt", 'w', encoding='utf-8')
        #f.write(str(text))
        #f.close()
        #os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
        #os.system("dot -Tpng "+ nombrearchivo +".txt -o " + nombrearchivo +".png")




menu()