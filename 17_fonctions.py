# Fonctions en Python

# Fonction simple
def saluer(nom):
    """Cette fonction salue une personne"""
    print(f"Bonjour {nom} !")

# Fonction avec paramètres et valeurs de retour
def addition(a, b):
    return a + b

# Fonction avec paramètres par défaut
def presenter(nom, age=25, ville="Dakar"):
    print(f"Je m'appelle {nom}, j'ai {age} ans et je vis à {ville}.")

# Appel des fonctions
saluer("Abdoul Rachid")

resultat = addition(15, 27)
print("Résultat :", resultat)

presenter("Abdoul")
presenter("Fatou")
presenter(age=30, nom="Moussa") # Arguments nommés.

# Fonction avec docstring (bonne pratique)
def carre(x):
    """Renvoie le carré d'un nombre"""
    return x**2

print("Carré de 8", carre(8))

# EXERCICE
def est_pair(nombre):
    """Vérifie si un nombre est pair ou non et renvoie un booléen."""
    if nombre % 2 == 0:
        return True
    else:
        return False
    
# ou 

def est_paire(nombre):
    """Renvoie True si le nombre est pair, False sinon"""
    return nombre % 2 == 0 # Plus pythonique

# Tests
print(est_pair(4)) # True
print(est_pair(7)) # False
print(est_pair(0)) # True


    
print(est_pair(4)) 

help(carre)