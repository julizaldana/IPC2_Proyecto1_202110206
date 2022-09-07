#NOMBRE: Julio Alejandro Zaldaña Ríos
#CARNET: 202110206
#IPC 2 - B
#PROYECTO 1

import os
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
        doc = minidom.parse(file)
        pacientes = doc.getElementsByTagName("paciente")
        print("----------------------------------------------------------")
        print("            Lista de Pacientes                 ")
        print("----------------------------------------------------------")
        for paciente in pacientes:                    
            nombre = paciente.getElementsByTagName("nombre")[0]
            print("Nombre: " + str(nombre.firstChild.data))
    
    elif respuesta=='2':
        exit()



menu()