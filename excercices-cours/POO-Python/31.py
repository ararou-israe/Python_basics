class cercle:
    def __init__(self,rayon):
        self._rayon=rayon
    @property
    def rayon(self):
        return self._rayon
    @property
    def aire(self):
        return 3.14*self._rayon**2
    @property
    def cercomference(self):
        return 2*3.14*self._rayon
cercle=cercle(5)   
print(f"rayon:{cercle.rayon}")
print(f"aire:{cercle.aire}")
print(f"cercomference:{cercle.cercomference}")
    