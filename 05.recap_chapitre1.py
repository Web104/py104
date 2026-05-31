# Programme récapitulatif

nom = input("Comment t'appelles-tu ? ")

while True:
    try:
        age = int(input("Quel est ton âge ? "))  # Conversion en entier
        break                                      # Si la conversion réussie, on sort.
    except ValueError:
        print("❌ Erreur : Veuillez entrer un nombre entier pour l'âge. ")

ville = input("Dans quelle ville habites-tu ? ")

print("\n--- Résumé ---")
print(f"Tu t'appelles {nom}")
print(f"Tu  as {age} ans.")
print(f"Tu vis as à {ville}.")

# Quelques calculs
print(f"Dans 10 ans tu auras {age + 10} ans.")
print(f"Tu es {'majeur' if age >= 18 else 'mineur'}.")

# Bonus : affichage avec formatage
print(f"\nBienvenue {nom.upper()} ! 🎉")