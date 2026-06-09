# utils/formatage.py 

def formater_telephone(telephone):
    """Nettoie et formate un numéro de téléphone"""
    chiffres = ''.join(filter(str.isdigit, telephone))

    if len(chiffres) == 10:
        return f"{chiffres[:2]} {chiffres[2:5]} {chiffres[5:8]} {chiffres[8:]}"
    elif len(chiffres) == 8:
        return f"{chiffres[:2]} {chiffres[2:4]} {chiffres[4:6]}  {chiffres[6:]}"
    return telephone

def formater_nom(nom):
    """Met le nom en forme correcte"""
    return nom.strip().title()