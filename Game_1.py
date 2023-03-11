import os
from Province import Province
from Edificio import Edificio
from Army import Army, Unit

provinces = [
    Province("Alphaland", 100),
    Province("Betatown", 200),
    Province("Crayville", 150),
    Province("Deltaville", 175),
    Province("Epsilonia", 125)
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()
    print("Seleccione una provincia:")
    for i, province in enumerate(provinces):
        print(f"{i+1}. {province.name}")

    opcion_provincia = input("Provincia seleccionada (0 para salir): ")

    try:
        opcion_provincia = int(opcion_provincia)
        if opcion_provincia == 0:
            break
        elif opcion_provincia < 1 or opcion_provincia > len(provinces):
            raise ValueError
    except ValueError:
        print("Opción inválida. Por favor, seleccione una provincia válida.")
        input("Presione enter para continuar...")
        continue

    provincia_seleccionada = provinces[opcion_provincia-1]

    while True:
        clear_console()
        print(f"Provincia: {provincia_seleccionada.name}")
        print(f"Recursos disponibles: {provincia_seleccionada.recursos}")
        print("Seleccione una opción:")
        print("1. Crear edificio")
        print("2. Crear ejército")
        print("3. Ver ejércitos")
        print("4. Volver a seleccionar provincia")

        opcion_menu = input("Opción seleccionada: ")

        if opcion_menu == "1":
            clear_console()
            nombre_edificio = input("Ingrese el nombre del edificio: ")
            costo_edificio = int(input("Ingrese el costo del edificio: "))
            if costo_edificio > provincia_seleccionada.recursos:
                print("No hay suficientes recursos para construir el edificio.")
            else:
                provincia_seleccionada.recursos -= costo_edificio
                # Aquí iría el código para crear el objeto Edificio
                print(f"Se construyó el edificio '{nombre_edificio}'.")
            input("Presione enter para continuar...")
        elif opcion_menu == "2":
            clear_console()
            nombre_ejercito = input("Ingrese el nombre del ejército: ")
            size_ejercito = int(input("Ingrese el tamaño del ejército: "))
            costo_ejercito = size_ejercito * 10 # Supongamos que cada unidad cuesta 10 recursos
            if costo_ejercito > provincia_seleccionada.recursos:
                print("No hay suficientes recursos para reclutar el ejército.")
            else:
                provincia_seleccionada.recursos -= costo_ejercito
                # Aquí iría el código para crear el objeto Army
                print(f"Se reclutó el ejército '{nombre_ejercito}'.")
            input("Presione enter para continuar...")
        elif opcion_menu == "3":
            clear_console()
            print(f"Ejércitos en la provincia {provincia_seleccionada.name}:")
            for army in provincia_seleccionada.army:
                print(f"Nombre: {army.name}, Tamaño: {army.size}")
            input("Presione enter para continuar...")
        elif opcion_menu == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione enter para continuar...")

