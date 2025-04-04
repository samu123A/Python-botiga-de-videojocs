1. Estructura General
Aquest codi és un sistema d'anàlisi per a una botiga de videojocs que llegeix dades d'un fitxer CSV (datos.csv) i ofereix diferents funcionalitats mitjançant un menú interactiu.

2. Funcions Principals
2.1. mostrar_menu()
Funció: Mostra un menú interactiu amb 4 opcions.

Flux:

Mostra les opcions disponibles.

L'usuari tria una opció (1-4).

Es crida a la funció corresponent segons l'opció seleccionada.

Si es tria "4", el programa es tanca.

2. 2. calcular_facturacio()
Objectiu: Calcula la facturació total de la botiga.

Process:

Llegeix el fitxer datos.csv.

Calcula:

Facturació sense IVA.

Facturació amb IVA.

Nombre total de productes venuts.

Nombre de productes diferents venuts.

Mostra els resultats en un format estructurat.

2. 3. mostrar_estoc()
Objectiu: Mostra l'estoc disponible de productes.

Process:

Llegeix el fitxer datos.csv.

Agrupa els productes per nom i categoria.

Suma les quantitats disponibles per a cada producte.

Mostra una taula amb:

Nom del producte.

Categoria.

Quantitat disponible.

2. 4. top_productes()
Objectiu: Mostra els 3 productes més venuts.

Process:

Llegeix el fitxer datos.csv.

Calcula per a cada producte:

Unitats venudes.

Facturació sense IVA.

Facturació amb IVA.

Ordena els productes per unitats venudes (de major a menor).

Mostra els 3 primers en una taula detallada.

3. Funcionament del Programa
Inici: S'executa mostrar_menu().

Lectura de dades: Totes les funcions llegeixen el mateix fitxer (datos.csv).

Interacció: L'usuari selecciona una opció i el programa executa la funció corresponent.

Sortida: El programa es tanca quan l'usuari tria l'opció 4.

4. Estructura del Fitxer CSV
El programa assumeix que datos.csv té les següents columnes:

Producte: Nom del producte.

Categoria: Categoria del producte.

Quantitat_Venuda: Unitats venudes.

Preu_Unitari: Preu sense IVA.

IVA: Percentatge d'IVA aplicable.

Estoc_Disponible: Unitats disponibles en estoc.