import os

class Province:
    def __init__(self, name):
        self.name = name
        self.army = []
        self.buildings = []


class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
def mostrar_opciones_edificios():
    print("Seleccione un edificio para construir:")
    print("1. Base del Ejército")
    print("2. Oficinas")
    print("3. Base Naval")


    
class Army:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.units = []

class Unit:
    def __init__(self, name, damage, defense):
        self.name = name
        self.damage = damage
        self.defense = defense



provinces = [
    Province("Alphaland"),
    Province("Betatown"),
    Province("Crayville"),
    Province("Deltaville"),
    Province("Epsilonia")
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        clear_console()
        print("Seleccione una provincia:")
        for i, province in enumerate(provinces):
            print(f"{i + 1}. {province.name}")
        provincia_seleccionada = input("Provincia seleccionada: ")
        try:
            provincia_seleccionada = int(provincia_seleccionada)
            if provincia_seleccionada < 1 or provincia_seleccionada > len(provinces):
                raise ValueError()
        except ValueError:
            print("Provincia inválida.")
            input("Presione Enter para continuar...")
            continue
        provincia_seleccionada = provinces[provincia_seleccionada - 1]
        
        while True:
            clear_console()
            print("Seleccione una acción:")
            print("1. Construir edificio")
            print("2. Continuar")
            print("3. Buildings")
            opcion_seleccionada = input("Opción seleccionada: ")
            try:
                opcion_seleccionada = int(opcion_seleccionada)
                if opcion_seleccionada < 1 or opcion_seleccionada > 2:
                    raise ValueError()
            except ValueError:
                print("Opción inválida.")
                input("Presione Enter para continuar...")
                continue
            
            if opcion_seleccionada == 1:
                mostrar_opciones_edificios()
                opcion_edificio = input("Opción seleccionada: ")
                try:
                    opcion_edificio = int(opcion_edificio)
                    if opcion_edificio < 1 or opcion_edificio > 3:
                        raise ValueError()
                except ValueError:
                    print("Opción inválida.")
                    input("Presione Enter para continuar...")
                    continue
                
                if opcion_edificio == 1:
                    edificio = Edificio("Base del Ejército")
                    provincia_seleccionada.buildings.append(edificio)
                    print("Base del Ejército construida en", provincia_seleccionada.name)
                    
                elif opcion_edificio == 2:
                    edificio = Edificio("Oficinas")
                    provincia_seleccionada.buildings.append(edificio)
                    print("Oficinas construidas en", provincia_seleccionada.name)
                    
                elif opcion_edificio == 3:
                    edificio = Edificio("Base Naval")
                    provincia_seleccionada.buildings.append(edificio)
                    print("Base Naval construida en", provincia_seleccionada.name)
                    
                input("Presione Enter para continuar...")
            elif opcion_seleccionada == 3:
                print("Buildings")
                building_selected = input("Seleccione un edificio para construir: ")
                try:
                    building_selected = int(building_selected)
                    if building_selected < 1 or building_selected > 3:
                        raise ValueError()
                except ValueError:
                    print("Opción inválida.")
                    input("Presione Enter para continuar...")
                    continue
                    
                if building_selected == 1:
                    new_building = Edificio("Army")
                    provincia_seleccionada.buildings.append(new_building)
                elif building_selected == 2:
                    new_building = Edificio("Office")
                    provincia_seleccionada.buildings.append(new_building)
                elif building_selected == 3:
                    new_building = Edificio("Naval")
                    provincia_seleccionada.buildings.append(new_building)
                    
                print(f"Se ha construido un edificio {new_building.nombre} en la provincia {provincia_seleccionada.name}")
                input("Presione Enter para continuar...")



menu_principal()
