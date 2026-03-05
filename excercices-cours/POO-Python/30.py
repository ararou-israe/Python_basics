class Personne:
    def __init__(self,nom,age):
            self._nom=nom
            self._age=age
     # getter pour le nom
    def get_age(self):
        return self._age
    # setter pour le nom
    def set_age(self,new):
        if new >= 0 and new <= 120:
            self._age = new
        else:
            print("age invalide") 
israe=Personne("israe",19)
print(israe.get_age())
israe.set_age(20)
print(israe.get_age())        