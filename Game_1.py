import os
from Province import Province
from Edificio import Edificio
from Army import Army, Unit

provinces = [
    Province("Alphaland"),
    Province("Betatown"),
    Province("Crayville"),
    Province("Deltaville"),
    Province("Epsilonia")
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
        print("Seleccione una opción:")
        print("1. Crear edificio")
        print("2. Crear ejército")
        print("3. Ver ejércitos")
        print("4. Volver a seleccionar provincia")

        opcion_menu = input("Opción seleccionada: ")

        if opcion_menu == "1":
            clear_console()
            nombre_edificio = input("Ingrese el nombre del edificio: ")
            # Aquí iría el código para crear el objeto Edificio
            input("Presione enter para continuar...")
        elif opcion_menu == "2":
            clear_console()
            nombre_ejercito = input("Ingrese el nombre del ejército: ")
            size_ejercito = input("Ingrese el tamaño del ejército: ")
            # Aquí iría el código para crear el objeto Army
            input("Presione enter para continuar...")
        elif opcion_menu == "3":
            clear_console()
            print(f"Ejércitos en la provincia {provincia_seleccionada.name}:")
            for army in provincia_seleccionada.army:
                print(f"{army.name} ({army.size} unidades)")
            input("Presione enter para continuar...")
        elif opcion_menu == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione enter para continuar...")
