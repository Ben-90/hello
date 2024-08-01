from datetime import date
import num2words
import sys 
class Seasons:
    def __init__(self, nbresjour):
        self.nbresjour = nbresjour
    
    def __repr__(self) -> str:
        return f"{self.nbresjour} minutes"
    
    @property
    def nbresjour(self):
        return num2words.num2words(self._nbresjour, lang='en')
    
    @nbresjour.setter
    def nbresjour(self, nbresjour):
        self._nbresjour = nbresjour * 24 * 60

def get_birth():
    try:
        birth = input("Enter your birthdate (YYYY-MM-DD): ").split("-")
        date_saisie = date(int(birth[0]), int(birth[1]), int(birth[2]))
        date_today = date.today()
        diff = int((date_today - date_saisie).days)
        return diff
    except ValueError:
        sys.exit("Invalid date")
    

def main():
    value = get_birth()
    season1 = Seasons(value)
    print(season1)

if __name__ == main():
    main()