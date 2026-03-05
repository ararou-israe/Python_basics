class vehicule:
    def __init__(self,marque,vitesse):
        self._marque = marque
        self._vitesse = vitesse
    def accelerer(self):
        print(f"{self._marque} accélère")
    def freiner(self):
        print(f"{self._marque} freine")
class voiture(vehicule):
    def __init__(self,marque,vitesse,portes):
        super().__init__(marque,vitesse)
        self._portes = portes
    def klaxonner(self):
        print(f"{self._marque} klaxonne")
ma_voiture = voiture("Toyota", 120, 4)
ma_voiture.accelerer()
ma_voiture.freiner()
ma_voiture.klaxonner()    