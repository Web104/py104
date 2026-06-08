# contact_utils.py

from datetime import datetime

def formater_telephone(telephone):
    """Nettoie et formate un numéro de téléphone"""
    # Supprime tous les caractères non numériques
    chiffres = ''.join(filter(str.isdigit, telephone))
    if len(chiffres) == 10:
        return f"{chiffres:2} {chiffres[2:4]} {chiffres[4:6]} {chiffres[6:8]} {chiffres[8:]}"
    return telephone

# def generer_id_contact():
#     """Génère un identifiant unique simple"""
#     annee = datetime.now().year
#     return f"CONT-{annee}-{len(contacts) + 1:03d}"

# Ce code s'exécute uniquement si on lance le fichier directement.
if __name__ == "__main__":
    print("=== Test du module contact_utils ===")
    print(formater_telephone("0145744747"))
    print(formater_telephone("0123456789"))

    