class personne:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email

    def se_presenter(self):
        return f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans. Mon email est {self.email}."
personne1 = personne("israe", 19, "israe@gmail.com")

print(f"nom:{personne1.nom}")
print(f"age:{personne1.age}")
print(f"email:{personne1.email}")

personne1.nom = "nisrine"
personne1.age +=1
personne1.email="nisrineararou@gmail.com"


print(f"nouveau nom:{personne1.nom}")
print(f"nouveau age:{personne1.age}")
print(f"nouveau email:{personne1.email}")
print(personne1.se_presenter())

