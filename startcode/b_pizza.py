class Pizza:
    def __init__(self,naam,grootte,toppings):
        self.naam = naam
        self.grootte = grootte
        self.toppings= toppings
        self.prijs = self.bereken_prijs()

    def toon_pizza(self):
        print("naam:", self.naam)
        print("grootte:", self.grootte)
        print("Toppings:", ", ".join(self.toppings))
        print("prijs:", self.prijs)

    def bereken_prijs(self):
        basisprijs = 0.00
        if self.grootte == "klein":
            basisprijs = 8.99
        elif self.grootte == "medium":
            basisprijs = 10.99
        elif self.grootte == "groot":
            basisprijs = 12.99

        toppingprijs = len(self.toppings)*1.50

        return basisprijs + toppingprijs

pizza1 = Pizza("Margherita", "medium", ["kaas", "tomatensaus"])
pizza2 = Pizza("Pepperoni", "groot", ["kaas", "tomatensaus", "pepperoni"])
pizza3 = Pizza("Hawaï", "klein", ["kaas", "tomatensaus", "ham", "ananas"])

pizza1.toon_pizza()
pizza2.toon_pizza()
pizza3.toon_pizza()