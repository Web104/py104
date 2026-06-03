# Exemple immuabilité

dimensions = (1920, 1080)   # tuple
# dimensions[0] = 3840      # Cela provoque une erreur (TypeError)

# Avec une liste (modifiable)
dimensions_liste = [1920, 1080]
dimensions_liste[0] = 3840
print(dimensions_liste)     # Modifié sans problème