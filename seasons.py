from datetime import date
import sys
class Seasons:
    def init():
        ...
    def __repr__(self) -> str:
        ...



def get_birth():
    try:
        birth = input("Enter your birthdate (YYYY-MM-DD): ").split("-")
        date_saisie = date(int(birth[0]), int(birth[1]), int(birth[2]))
        return (date.today().year - date_saisie.year())
    except ValueError:
        sys.exit("Invalid date")
    

def main():
    get_birth()

if __name__ == main():
    main()