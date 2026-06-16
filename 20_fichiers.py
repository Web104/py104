# Manipulation de fichiers

# 1. Ecrire dans un fichier 
with open("mon_fichier.txt", "a", encoding="utf-8") as f:
    f.write("Bonjour le monde !\n")
    f.write("Ceci est ma première ligne écrite depuis Python. \n")
    f.writelines(["Pyton est génial\n", "On continue d'apprendre\n "])

print("✅ Fichier écrit avec succès !")

# 2. Lire le fichier
with open("mon_fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

    print("\nContenu du fichier :")
    print(contenu) 

# 3. Lire ligne par ligne 
print("\nLecture ligne par ligne :")
with open("mon_fichier.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(f"Ligne : {ligne.strip()}")

# Test des modes w et a

# Mode écriture (écrase)
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Première écriture. \n")

# Mode ajout
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("Cette ligne est ajoutée. \n")

with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
    