fruits = ["pomme", "banane", "orange"]

# Mauvaise copie (référence)
copie1 = fruits
copie1[0] = "cerise"
print("Après modification de copie1 :", fruits) # fruits est aussi modifier.

# Bonne copie
fruits = ["pomme", "banane", "orange"] # réinitialisons
copie2 = fruits[:] # ou fruits.copy()
copie2[0] = "cerise"
print("Après modification de copie2 :", fruits) # fruits reste intact.
