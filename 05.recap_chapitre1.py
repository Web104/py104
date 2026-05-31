# Programme récapitulatif

nom = input("Comment t'appelles-tu ? ")
age = int(input("Quel est ton âge ? "))  # Conversion en entier
if type(age) == str:
    print("Veuillez entrer un âge valide !")
    print(age)
ville = input("Dans quelle ville habites-tu ? ")

print("\n--- Résumé ---")
print(f"Tu t'appelles {nom}")
print(f"Tu  as {age} ans.")
print("Tu vis as à {ville}.")

# Quelques calculs
print(f"Dans 10 ans tu auras {age + 10} ans.")
print(f"Tu es {'majeur' if age >= 18 else 'mineur'}.")

# Bonus : affichage avec formatage
print(f"\nBienvenue {nom.upper()} ! 🎉")