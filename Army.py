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
