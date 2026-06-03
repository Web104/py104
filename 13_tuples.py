# Les Tuples

# Création
point = (3, 7)
couleurs = ("rouge", "vert", "bleu")
personne = ("Abdoul", 24, "Dakar")

print("Tuple point :", point)
print("Première couleur :", couleurs [0])

# Déballage (unpacking)  très utile
nom, age, ville = personne
print(f"{nom} a {age} ans et vit à {ville}")

# Pourquoi utilisons nous un tuple plutôt qu'une liste ?
# Ex: coordonnées qui ne doivent pas changer
dimensions = (1920, 1080)

# Tentative de modification (va générer une erreur)
# dimensions[0] = 3840 # TypeError

# Tuple à un seul élément (attention à la syntaxe)
singleton = (5) # pas (5)
print("Tuple singleton :",  singleton)