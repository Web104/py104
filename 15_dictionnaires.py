# Les Dictionnaires

from datetime import datetime

nowk = datetime.now()
annee = nowk.year

# Création
personne = {
    "nom": "Abdoul Rachid",
    "age": 24,
    "ville": "Dakar",
    "est_etudiant": True,
    "langages": ["Python", "Php", "JavaScript"]
}

print("Dictionnaire complet :", personne)
print("Nom :", personne["nom"])
print("Âge :", personne["age"])

# Ajout / Modification
personne["profession"] = "Développeur en formation"
personne["age"] = 25

print(personne["annee_naissance"])
print("\nAprès modification :", personne)

# Parcours d'un dictionnaire
print("\n=== Clés et valeurs ===")
for cle, valeur in personne.items():
    print(f"{cle} -> {valeur}")

# Vérification d'existence
if "ville" in personne:
    print("\nLa clé 'ville' existe")