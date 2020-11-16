#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    fi = open('notas.txt', 'r')
    with open('notas.txt') as fi:
        for line in fi:
            cantidad_lineas += 1
    print(f"el archivo tiene {cantidad_lineas} lineas")

    fi.close()


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)
    fi = open('notas.txt', 'r')
    fo = open('nuevo.txt', 'w')
    with open('notas.txt') as fi:
        for line in fi:
            fo.write(line)
            cantidad_lineas += 1
    print(f"se copiaron {cantidad_lineas} lineas al archivo nuevo")
    fi.close()
    fo.close()


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''

    ambientes_2 = 0
    ambientes_3 = 0

    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    total_Departamento = len(data)
    for i in range(total_Departamento):
        row = data[i]
        ambientes = str(row.get('ambientes'))
        if ambientes == '2':
            ambientes_2 += 1
        if ambientes == '3':
            ambientes_3 += 1

    print(f"hay {ambientes_2} departamentos de 2 ambientes")
    print(f"hay {ambientes_3} departamentos de 3 ambientes")


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"
    print("inventario frutas y verduras\n"
          "para finalizar escriba FIN en el nombre del producto")
    while True:
        fruta_verdura = str(input("escriba el nombre de su producto\n"))
        if fruta_verdura == "FIN":
            break
        total = int(input("escriba el total\n"))
        inventario[fruta_verdura] = total
    print(inventario)


def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio,
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})
    print("inventario de frutas y verduras, archivo csv\n"
          "para finalizar escriba FIN en el nombre del producto")
    inventario = open('inventario.csv', "w", newline='')
    header = ["fruta/verdura", "cantidad"]
    writer = csv.DictWriter(inventario, fieldnames=header)
    writer.writeheader()
    while True:
        fruta_verdura = str(input("ingrese fruta o verdura\n"))
        if fruta_verdura == "FIN":
            break
        cantidad = int(input("ingrese la cantidad\n"))
        writer.writerow({"fruta/verdura": fruta_verdura, "cantidad": cantidad})
    inventario.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
