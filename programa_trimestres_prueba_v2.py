import csv
from os import system

def cargar_archivo():
    lista = []
    ruta_archivo = input("Ingrese la ruta al archivo .csv: ")
    try:
        with open(ruta_archivo, "r", newline="") as archivo:
            lectorCsv = csv.reader(archivo, delimiter=";")
            next(lectorCsv)  # Salta la primera línea (cabecera)
            for linea in lectorCsv:
                # Asegúrate de manejar valores vacíos
                anno = int(linea[0]) if linea[0] else 0
                trimestre1 = int(linea[1]) if linea[1] else 0
                trimestre2 = int(linea[2]) if linea[2] else 0
                trimestre3 = int(linea[3]) if linea[3] else 0
                trimestre4 = int(linea[4]) if linea[4] else 0
                
                lista.append({
                    'Año': anno,
                    'Trimestre 1': trimestre1,
                    'Trimestre 2': trimestre2,
                    'Trimestre 3': trimestre3,
                    'Trimestre 4': trimestre4
                })

        # Ordena la lista de diccionarios por año
        lista.sort(key=obtener_anno)
        return lista

    except FileNotFoundError:
        print("El archivo no existe. Por favor, verifique la ruta e inténtelo de nuevo.")
        return []
    except ValueError:
        print("Error en la conversión de datos. Verifique el formato del archivo.")
        return []

def obtener_anno(entrada):
    return entrada['Año']

def menu_principal(lista):
    opciones = {
        '1': ('Imprimir años con media: ', accion1),
        '2': ('Guardar años cronológicamente', lambda: accion2(lista)),
        '3': ('Salir', salir)
    }

    generar_menu(opciones, '3')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def accion1():
    print('Has elegido la opción Imprimir años con media.\n')
    print("Año\t\tTrimestre 1\t\tTrimestre 2\t\tTrimestre 3\t\tTrimestre 4")
    for anno in lista:
        print(f"{anno['Año']}\t\t{anno['Trimestre 1']}\t\t{anno['Trimestre 2']}\t\t{anno['Trimestre 3']}\t\t{anno['Trimestre 4']}")
    input()

def accion2(lista):
    print('Has elegido la opción Guardar años cronológicamente.\n')
    archivo_salida = input("Ingrese la ruta donde guardará el archivo: ")
    with open(archivo_salida, 'w', newline="") as archivo:
        escritorCsv = csv.writer(archivo, delimiter=";")
        escritorCsv.writerow(['Año', 'Trimestre 1', 'Trimestre 2', 'Trimestre 3', 'Trimestre 4'])
        for anno in lista:
            escritorCsv.writerow([anno['Año'], anno['Trimestre 1'], anno['Trimestre 2'], anno['Trimestre 3'], anno['Trimestre 4']])
    print(f"Se ha creado exitosamente el archivo en {archivo_salida}")
    input()

def salir():
    print('Saliendo')

# Ejecución de la función
lista = cargar_archivo()
menu_principal(lista)
