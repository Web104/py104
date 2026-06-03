# Les listes en Python

# Création d'une liste
fruits = ["pomme", "banane", "orange", "mangue", "ananas"]

print("Liste complète :", fruits)
print("Premier fruit :", fruits[0])
print("Dernier fruit :", fruits[-1])
print("Nombre de fruits :", len(fruits))

# Modification
fruits[1] = "banane verte"
print("Après modification :", fruits)

# Ajout et suppression
fruits.append("kiwi") # ajoute à la fin
fruits.insert(2, "fraise") # insère à la position 2
print("Après ajout :", fruits)

supprime = fruits.pop() # retire le dernier
print("Elément supprimé :", supprime)
print("Après suppression :", fruits)

delete_fraise = fruits.pop(2)
print("Liste après suppression de fraise :", fruits)

# Parcours de liste
print("\n=== Parcours avec for ===")
for fruit in fruits:
    print(f"- {fruit.capitalize()}")

# Vérification d'appartenance
if "pomme" in fruits:
    print("\nLa pomme est dans la liste !")
    