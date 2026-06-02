# Boucles avancées

print("=== Utilisation de break et continue ===\n")

# Exemple break
for i in range(10):
    if i == 5:
        break       # Arrête complètement la boucle
    print(i, end=" ")
print(" -> break à 5\n")

# Exemple continue
for i in range(10):
    if i % 2 == 0:
        continue    # Saute l'itération actuelle
    print(i, end=" ")
print(" -> seuls les impairs\n")

# Exemple avec else sur une boucle
print("\n=== Boucle avec else ===")
nombre = 4

for  i in range(2, nombre):
    if nombre % i == 0:
        print(f"{nombre} n'est pas premier")
        break
else:
    print(f"{nombre} est un nombre premier !")


