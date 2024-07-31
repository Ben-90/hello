import inflect
import sys

p = inflect.engine()

noms = []
while True:
    try:
        nom = input("Name :")
        noms +=[nom]

    except EOFError:
        break
print(f"\n Adieu, adieu to {p.join(noms)}")
    

