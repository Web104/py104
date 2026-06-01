# conditions plus avancées

# 1. Opérateurs de comparaison
x = int(input("Entre un nombe entier : "))

if x> 0:
    print(f"{x} est positif")
elif x < 0:
    print(f"{x} est négatif")
else:
    print("Tu as entré zéro.")

# 2. Conditions multiples avec and / or
age = int(input("\nQuel est ton âge ?"))
has_permis = input("As-tu le permis de conduire ? (oui/non)").strip().lower()

if age >=18 and has_permis == "oui":
    print("Tu peux conduire légalement")
elif age >= 18 and has_permis == "non":
    print("Tu es majeur mais tu n'as pas encore le permis.")
elif age < 18:
    print("Tu es encore mineur.")
else:
    print("Réponse invalide.")

# 3. Condition avec in (très utile en Python)
fruit = input("\nEntre un fruit (pomme, banane, orange)").strip().lower()

if fruit in ["pomme", "banane", "orange"]:
    print(f"{fruit.capitalize()} est dans la liste.")
else:
    print("Ce fruit n'est pas dans la liste.")

nbre = 4 # Tester avec 0, 8, 9, 5, 4

if nbre % 2 == 0:
    print(f"{nbre} est un nombre pair.")
else:
    print(f"{nbre} n'est pas pair.")