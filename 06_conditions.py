# Structures conditionnelles

age = int(input("Quel est ton âge ?"))

if age < 18:
    print("Tu es mineur.")
elif age >= 18 and age <= 65:
    print("Tu es majeur et en âge de travailler.")
elif age >= 65:
    print("Tu es à la retraite.")
else:
    print("Âge invalide.")

# Condition avec opérateur logique
temperature = float(input("\nQuelle est la température actuelle ?"))

if temperature > 30:
    print("Il fait très chaud.")
elif temperature < 0:
    print("Il fait très froid")
else:
    print("Température agréable.")
