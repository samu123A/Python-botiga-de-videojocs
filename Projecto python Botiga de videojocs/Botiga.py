    
import csv
from datetime import datetime

def mostrar_menu():
    while True:
        print("\n" + "="*50)
        print("SISTEMA D'ANALITIQUES - BOTIGA DE VIDEOJOCS")
        print("="*50)
        print("1. Calcular facturació total")
        print("2. Mostrar estoc disponible")
        print("3. Top 3 productes més venuts")
        print("4. Sortir")
        print("="*50)
        
        opcio = input("Selecciona una opció (1-4): ")
        
        if opcio == "1":
            calcular_facturacio()
        elif opcio == "2":
            mostrar_estoc()
        elif opcio == "3":
            top_productes()
        elif opcio == "4":
            print("Gràcies per utilitzar el sistema. Fins aviat!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció del 1 al 4.")
