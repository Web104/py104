# Saisie utilisateur

prenom = input("Quel est ton prénom ?")
age = input("Quel est ton âge ?")

print(f"\nBonjour {prenom}")
print(f"Tu as {age} ans.")

# Important : input() renvoie toujours une chaîne de caractères str
print("Type de age :", type(age))

# Conversion de type 
# age = int(age)      # Conversion en entier
print("Type de age après conversion :", type(age))
print(f"Dans 5 ans, tu auras {age + 5} ans.")
