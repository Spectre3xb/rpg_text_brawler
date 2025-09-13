class Player:
    def __init__(self, name, attack, defense, cons, prof):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cons = cons
        self.prof = prof
        self.hp = cons * 100
