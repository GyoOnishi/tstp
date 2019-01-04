class Horse:
    def __init__(self, name):
        self.name = name

class Rider:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

the_horse = Horse('Hack')
the_rider = Rider('Tom', the_horse)

print(the_rider.horse.name)
