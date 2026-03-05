# excercice
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficherInfos(self):
        print("nom:", self.nom)
        print("age:", self.age)

class Salarie(Personne):
    def __init__(self, nom, age, numeroSomme, salaire):
        super().__init__(nom, age)
        self.numeroSomme = numeroSomme
        self.salaire = salaire

    def calculerSalaire(self):
        return self.salaire

    def afficherInfos(self):
        super().afficherInfos()
        print("Numero :", self.numeroSomme)
        print("Salaire:", self.salaire)


class Etudiant(Personne):
    def __init__(self, nom, age, cne, notes):
        super().__init__(nom, age)
        self.cne = cne
        self.notes = notes

    def calculerMoyenne(self):
        return sum(self.notes) / len(self.notes)

    def afficherInfos(self):
        super().afficherInfos()
        print("CNE:", self.cne)
        print("Notes:", self.notes)


class Doctorant(Salarie, Etudiant):
   
    def __init__(self, nom, age, numeroSomme, salaire, cne, notes, departement, anneeInscription):
        super().__init__(nom, age, numeroSomme, salaire)
        self.cne = cne
        self.notes = notes
        self.departement = departement
        self.anneeInscription = anneeInscription

    def afficherInfos(self):
        super().afficherInfos()
        print("ton Numero est  :", self.numeroSomme)
        print("ton Salaire est:", self.salaire)
        print("votre CNE est:", self.cne)
        print("vos Notes:", self.notes)
        print("votre Departement est:", self.departement)
        print("Annee Inscription:", self.anneeInscription)

d = Doctorant("israe", 21, "212", 1000000, "L679861", [18, 14, 17.6], "Informatique", 2025)

d.afficherInfos()
print("votre moyenne est:", d.calculerMoyenne())
print(" ton Salaire:", d.calculerSalaire())