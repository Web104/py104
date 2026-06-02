# Boucles en Python

print("=== Boucle while ===")
compteur = 0

while compteur < 5:
    print(f"Compteur = {compteur}")
    compteur += 1 # équivalent à compteur = compteur + 1

print("\n=== Boucle for avec range() ===")
for i in range(5): # 0 à 4
    print(f"Valeur de i = {i}")

print("\n=== For avec une liste ===")
fruits = ["pomme","banane","orange","manggue","ananas","papaye"]

for fruit in fruits:
    print(f"J'aime les {fruit}s")

# Exemple combiné : conditions + boucle
print("\n=== Nombres pairs entre 1 et 20 ===")
for nombre in range(1, 21):
    if nombre % 2 == 0:
        print(nombre, end=" ") # end=" " pour afficher sur la même ligne

# Exemple pour afficher uniquement les nombres  impairs. 
print(" ")
print("=== Nombres impairs entre 1 et 21 ===")
for nombre in range(1, 21):
    if nombre % 2 == 1:
        print(nombre, end=" ")