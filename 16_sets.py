# Les Ensembles 

# Création 
fruits = {"pomme", "banane", "orange", "pomme"} # doublon supprimé automatiquement
print("Set fruits :", fruits)
print("Nombre d'éléments :", len(fruits))

# Ajout et suppression
fruits.add("mangue")
fruits.discard("pomme")     # supprime sans erreur si absent
print("Après modification :", fruits)

# Opérations mathématiques
legumes = {"carotte", "tomate", "pomme de terre", "banane"}

print("\nUnion :", fruits | legumes)
print("\nIntersection :", fruits & legumes)
print("\nDifférence :", fruits - legumes)

# Vérification 
if "orange" in fruits:
    print("\nL'orange est dans le set.")
