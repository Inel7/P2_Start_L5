class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")

kat = Dier("kat","miauw")
hond = Dier("hond", "woef")
koe = Dier("koe","boe")

kat.maak_geluid()
hond.maak_geluid()
koe.maak_geluid()