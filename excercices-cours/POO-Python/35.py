class vehicule:
    def demarrer(self):
        print("Le véhicule démarre")
class voiture(vehicule):
    def demarrer(self):
        print("La voiture démarre")
class moto(vehicule):
    def demarrer(self):
        print("La moto démarre") 
vehicules=[voiture(),moto()]
for v in vehicules:
    v.demarrer()                       