class personne:
    def __init__(self,nom,age):
        self._nom=nom
        self._age=age
   
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new):
        if not isinstance(new,int):
            raise TypeError("age doit etre un entier")
        if new < 0 :
            raise ValueError("age doit etre positif")
        if new > 120:
            raise ValueError("age doit etre inferieur a 120")
        self._age = new
