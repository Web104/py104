# utils/validation.py

def is_valide_email(email):
    """Vérifie si l'email semble valide (très basique)"""
    return "@" in email and "." in email

def is_valide_telephone(telephone):
    """Vérifie si le téléphone contient uniquement des chiffres"""
    chiffres = ''.join(filter(str.isdigit, telephone))
    return len(chiffres) >= 8
