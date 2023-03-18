# CSV y Python con List
# Escribir archivo

import csv

contactos = [
    ("Nombre", "Puesto", "Email"),
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Consultora Python", "marta@ejemplo.com")
]

with open("contactos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo, delimiter=",")
    for contacto in contactos:
        escritor.writerow(contacto)

# Leer archivo
# CSV Lectura, puede ser como un List

with open("contactos.csv", newline="") as archivo:
    lector = csv.reader(archivo, delimiter=",")
    lista = list(lector)
    con=0
  #  for elemento in lista:
  #      print(elemento[0])
  #      print(elemento[1])
  #      print(elemento[2])    
        
nuevoValor="Manuel"        
for elemento in lista:
    if elemento[0]==nuevoValor:
        elemento[0]="Gustavo"

for elemento in lista:
    print(elemento[0])