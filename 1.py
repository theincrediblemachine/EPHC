# vraag de gebruiker om zijn naam en leeftijd, geef de gebruiker het jaar terug waarin ze 100 worden
# 2018 + (100 - user_age) = jaar wanneer ze 100 worden
# bonus 1: vraag om een getal en print de zin zoveel keer uit
# bonus 2: print de zinnen op verschillende regels uit

import os

naam = input("Wat is je naam?\n")
age = int(input("Hoe oud ben je?\n"))
som = 2018 + (100 - age)
poep = f"In {som} wordt je 100 jaar oud!\n"
print(poep)
i = input("Geef me een nummer\n")
print(poep*int(i))