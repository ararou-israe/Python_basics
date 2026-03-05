class personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans."
personne1 = personne("israe", 19)
personne2 = personne("nisrine", 22)
personne3 = personne("raniia", 17)

print(personne1.se_presenter())
print(personne2.se_presenter())
print(personne3.se_presenter())