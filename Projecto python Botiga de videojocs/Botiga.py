    
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
    with open('dades_botiga.csv', mode='r', encoding='utf-8') as file:
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
def mostrar_estoc():
    with open('dades_botiga.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        estoc = {}
        
        for row in reader:
            producte = row['Producte']
            categoria = row['Categoria']
            quantitat = int(row['Estoc_Disponible'])
            
            if producte in estoc:
                estoc[producte]['quantitat'] += quantitat
            else:
                estoc[producte] = {
                    'categoria': categoria,
                    'quantitat': quantitat
                }
        
        print("\n" + "="*50)
        print("ESTOC DISPONIBLE")
        print("="*50)
        print("{:<40} {:<20} {:<10}".format("Producte", "Categoria", "Quantitat"))
        print("-"*70)
        
        for producte, info in sorted(estoc.items()):
            print("{:<40} {:<20} {:<10}".format(
                producte, 
                info['categoria'], 
                info['quantitat']
            ))
        
        print("="*70)
def top_productes():
    with open('dades_botiga.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        productes = {}
        
        for row in reader:
            nom_producte = row['Producte']
            quantitat = int(row['Quantitat_Venuda'])
            preu = float(row['Preu_Unitari'])
            iva = float(row['IVA'])
            
            if nom_producte in productes:
                productes[nom_producte]['quantitat'] += quantitat
                productes[nom_producte]['facturacio_sense_iva'] += quantitat * preu
                productes[nom_producte]['facturacio_amb_iva'] += quantitat * preu * (1 + iva/100)
            else:
                productes[nom_producte] = {
                    'categoria': row['Categoria'],
                    'quantitat': quantitat,
                    'facturacio_sense_iva': quantitat * preu,
                    'facturacio_amb_iva': quantitat * preu * (1 + iva/100)
                }
        
        top3 = sorted(
            productes.items(), 
            key=lambda x: x[1]['quantitat'], 
            reverse=True
        )[:3]
        
        print("\n" + "="*50)
        print("TOP 3 PRODUCTES MÉS VENUTS")
        print("="*50)
        print("{:<5} {:<40} {:<20} {:<15} {:<20} {:<20}".format(
            "Pos.", "Producte", "Categoria", "Unitats venudes", "Facturació (s/IVA)", "Facturació (c/IVA)"))
        print("-"*120)
        
        for i, (producte, info) in enumerate(top3, 1):
            print("{:<5} {:<40} {:<20} {:<15} {:<20.2f}€ {:<20.2f}€".format(
                i,
                producte,
                info['categoria'],
                info['quantitat'],
                info['facturacio_sense_iva'],
                info['facturacio_amb_iva']
            ))
        
        print("="*120)

if __name__ == "__main__":
    with open('dades_botiga.csv', mode='r', encoding='utf-8'):
        pass
    mostrar_menu()
