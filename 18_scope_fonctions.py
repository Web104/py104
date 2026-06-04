# Portée des variables(Scope)

from datetime import datetime

x = 10  # Variables globale

def ma_fonction():
    """Exploration des portée en python"""
    y = 5
    print("x à l'intérieur de la fonction :", x)
    print("y à l'intérieur de la fonction :", y)

ma_fonction()

print("x en dehors :", x)
# print(y)    # Erreur car y n'existe pas en dehors e la fonction.

# EXERCICE
nowk = datetime.now()
annee = nowk.year
print(annee)

def calculer_age(your_year):
    return annee - your_year

print("Vous avez", calculer_age(your_year=2002), "ans")