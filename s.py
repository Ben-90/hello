class Sae:
    def __init__(self, prix):
        self.prix = prix
    
    def __repr__(self) -> str:
        return f"le double du prix est {self.prix}"
    
    @property
    def prix(self):
        return self._prix
    
    @prix.setter
    def prix(self, prix):
        self._prix = prix * 2

sae = Sae(100)
print(sae)





from datetime import date
import sys
class Seasons:
    def init(self, nbresdate):
        
        self.nbresdate = nbresdate
    #def __repr__(self) -> str:
    #    return f"Seasons(nbres_dates={self.nbres_dates})"
    
    @property
    def nbresdate(self):
        return f'{self._nbresdate}'
    
    @nbresdate.setter
    def nbresdate(self, nbresdate):
        self._nbresdate = nbresdate * 24 * 60




def main():
    #diff = get_birth()
    season = Seasons(123)
    print(season)

if __name__ == main():
    main()