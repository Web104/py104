# Listes avancées

fruits = ["pomme", "banane", "orange", "mangue", "ananas", "kiwi", "fraise"]

# 1. Slicing (découpage)

print("Les 3 premiers :", fruits[:3])
print("Du 2e au 5e :", fruits[1:5])
print("Les 3 derniers :", fruits[-3:])
print("Tous sauf le premier :", fruits[1:])

# 2. Copie de liste
copie = fruits[:]       # bonne façon de copier
copie[0] = "cerise"
print("\nListe originale :", fruits)
print("Copie modifiée :", copie)

# 3. Listes en compréhension (très pythonique !)
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

carres = [x**2 for x in nombres]

# ou
carrees = []
for x in nombres:
    carrees.append(x**2)

pairs = [x for x in nombres if x % 2 == 0]
mots_long = [fruit.upper() for fruit in fruits if len(fruit) > 5]

print("\nCarrés :", carres)
print("Nombres pairs :", pairs)
print("Fruits longs en majuscules :", mots_long)

# Listes en compréhension qui contient les cubes des nombres impairs de 1 à 20

nbre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

cubes_nbre_impairs = [x**3 for x in nbre if x % 2 != 0]

print("Cubes des nombres impairs :", cubes_nbre_impairs)

# Version améliorée
cubes_impairs = [x**3 for x in range(1, 21) if x % 2 != 0]
print("Cubes des nombres impairs :", cubes_impairs)
