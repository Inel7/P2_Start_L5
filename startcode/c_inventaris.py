class Auto:
    def __init__(self,merk,model,jaar):
        self.merk=merk
        self.model=model
        self.jaar=jaar


class Inventaris:
    def __init__(self):
        self.wagens = []

    def voeg_auto_toe(self,auto):
        self.wagens.append(auto)

    def verwijder_auto(self,auto):
        if auto in self.wagens:
            self.wagens.remove(auto)
        else:
            print("auto niet gevonden")

    def toon_inventaris(self):
        for auto in self.wagens:
            print(f"{auto.merk} {auto.model} ({auto.jaar})")



inventaris = Inventaris()
auto1 = Auto("Volvo", "V40", 2018)
auto2 = Auto("Toyota", "Supra", 2006)

inventaris.voeg_auto_toe(auto1)
inventaris.voeg_auto_toe(auto2)
inventaris.toon_inventaris()

inventaris.verwijder_auto(auto1)
inventaris.toon_inventaris()