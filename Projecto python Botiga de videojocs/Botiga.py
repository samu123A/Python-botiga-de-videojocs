    
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
def calcular_facturacio():
    with open('datos.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        facturacio_sense_iva = 0.0
        facturacio_amb_iva = 0.0
        total_productes_venduts = 0
        productes_diferents = set()
        
        for row in reader:
            quantitat = int(row['Quantitat_Venuda'])
            preu = float(row['Preu_Unitari'])
            iva = float(row['IVA'])
            
            preu_sense_iva = quantitat * preu
            preu_amb_iva = preu_sense_iva * (1 + iva/100)
            
            facturacio_sense_iva += preu_sense_iva
            facturacio_amb_iva += preu_amb_iva
            total_productes_venduts += quantitat
            productes_diferents.add(row['Producte'])
        
        print("\n" + "="*50)
        print("INFORME DE FACTURACIÓ")
        print("="*50)
        print(f"Productes diferents venuts: {len(productes_diferents)}")
        print(f"Unitats totals venudes: {total_productes_venduts}")
        print(f"Facturació total sense IVA: {facturacio_sense_iva:.2f}€")
        print(f"Facturació total amb IVA: {facturacio_amb_iva:.2f}€")
        print("="*50)
