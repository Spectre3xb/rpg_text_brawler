class Player:
    def __init__(self, name, attack, defense, cons, prof, weapons):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cons = cons
        self.prof = prof
        self.hp = cons * 100
        self.weapons = weapons

    def level_up(self):
        self.attack += 5
        self.defense += 5
        self.cons += 5
        self.prof += 5
        self.hp = self.cons * 100

    def damage(self, damage):
        self.hp -= damage
