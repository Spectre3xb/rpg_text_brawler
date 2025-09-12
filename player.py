class Player:
    def __init__(self, name, strength, dext, cons, prof):
        self.name = name
        self.strength = strength
        self.dext = dext
        self.cons = cons
        self.prof = prof
        self.hp = cons * 100
