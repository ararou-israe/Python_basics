from abc import ABC ,abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass                
    @abstractmethod
    def descreption(self):
        pass
    def __add__(self, other):
        return print(f" {self.descreption()}+{other.descreption()} : {self.cout()+other.cout()}")
    def commande(self):
        return print(f"commande : {self.descreption()} \n prix : {self.cout()}dh")



class cafe(Boisson):
    def cout(self):
        return 2.00
    def descreption(self):
        return "cafe simple"
class the(Boisson):
    def cout(self):
        return 15
    def descreption(self):
        return "the"
 
class DecorateurBoisson(Boisson):
    def __init__(self,boisson):
        self._boisson=boisson
 # ajout de lait
class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.5
    def descreption(self):
        return self._boisson.descreption()+" , lait"
 # ajout de sucre
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.2
    def descreption(self):
        return self._boisson.descreption()+", sucre"
# ajout de caramel   
class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+5
    def descreption(self):
        return self._boisson.descreption()+" , caramel"

# 1er test
print("1er test")
boisson  = cafe()
print(boisson.descreption())
print(boisson.cout())
boisson2=the()
# tester operateur add
print("test de l operateur add")
print(boisson+boisson2)
print(" test de la classe decorateur")
boisson=Lait(boisson)
print(boisson.descreption())
print(boisson.cout())
boisson= Sucre(boisson)
print(boisson.descreption())
print(boisson.cout())
# test de la methode commande
boisson.commande()



    
@dataclass
class Client:
    nom:str
    numero:int
    points_fidelite:int    
    

class Commande:
    def __init__(self, client, list_boissons):
        self.client = client
        self.list_boissons = list_boissons
    def ajouterBoisson(self, boisson):
        self.list_boissons.append(boisson)

    def  prix_total(self):
        total = 0
        for boisson in self.list_boissons:
            total += boisson.cout()
        return total
    def afficherCommande(self):
        pass
class CommandeSurPlace(Commande):
    def afficherCommande(self):
        print(f"Commande sur place pour le client {self.client.nom} :")
        for boisson in self.list_boissons:
            print(f"- {boisson.descreption()} : {boisson.cout()} dh")
        print(f"Prix total : {self.prix_total()} dh")
        
class CommandeEmporter(Commande):
    def afficherCommande(self):
        print(f"Commande emporter pour le client {self.client.nom} :")
        for boisson in self.list_boissons:
            print(f"- {boisson.descreption()} : {boisson.cout()} dh")
        print(f"Prix total : {self.prix_total()} dh")

class Fidelite:
    def ajouter_fidelite(self,client,fidelite):
        client.points_fidelite+=fidelite

class CommandeFidele(Commande,Fidelite):
    def ajouter_fidelite(self,client,fidelite,commande):
        super().ajouter_fidelite(client,fidelite)
        print(f"Fidelite ajoutée : {fidelite} points pour le client {client.nom}")                


#tester les classes Commande et Fidelite
# creer plusieurs clients et plusieurs boissons 
print("\n\n2eme test:\n")
client1=Client("israe", 123456789, 0)
client2=Client("nisrine", 987654321, 0)
client3=Client("mohamed", 555555555, 2)
client4=Client("sara", 111111111, 5)
boisson1=cafe()
boisson2=the()
boisson4=Lait(boisson)
boisson4=Sucre(boisson)
boisson3=Sucre(boisson)
boisson5=Caramel(boisson)


# creer des commandes pour les clients et afficher les commandes et les points de fidelite apres chaque commande
commande1=CommandeSurPlace(client1,[boisson1,boisson2])
commande1.afficherCommande()
print(f"ajout de fidelite: ")
commande_fidele=CommandeFidele(client1,[boisson1,boisson2])
commande_fidele.ajouter_fidelite(client1,5,commande1)
print(f"points de fidelite du client {client1.nom} : {client1.points_fidelite}")

commande2=CommandeEmporter(client1,[boisson3,boisson4,boisson5])
commande2.afficherCommande()
print(f"ajout de fidelite: ")
commande_fidele.ajouter_fidelite(client1,10,commande2)
print(f"points de fidelite du client {client1.nom} : {client1.points_fidelite}")

commande3=CommandeSurPlace(client2,[boisson1,boisson2,boisson3])
commande3.afficherCommande()
print(f"ajout de fidelite: ")
commande_fidele.ajouter_fidelite(client2,15,commande3)
print(f"points de fidelite du client {client2.nom} : {client2.points_fidelite}")


    

    