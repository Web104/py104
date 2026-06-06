# PROJET RECAPITULATIF

from colorama import init, Fore, Back, Style
import json
import os

init(autoreset=True)

# Nom du fichhier de sauvegarde
FICHIER_CONTACTS = "contacts.json"

# Charger les contacts au démarrage
def charger_contacts():
    global contacts
    if os.path.exists(FICHIER_CONTACTS):
        try:
            with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
                contacts = json.load(f)
            print(f"✅ {len(contacts)} contacts chargés depuis le fichier.")
        except:
            print("⚠️ Erreur lors du chargement du fichier. Démarrage avec liste vide.")
            contacts = []
    else:
        contacts = []

# Sauvegarder les contacts
def sauvegarder_contacts():
    try:
        with open(FICHIER_CONTACTS, 'w', encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
    except:
        print("❌ Erreur lors de la sauvegarde.")


charger_contacts()

# Ajouter un contact
def ajouter_contact():
    """Ajoute un nouveau contact dans la liste"""
    print("\n--- Ajout d'un nouveau contact")

    nom = input("Entrez le nom :").strip().title()
    telephone = input("Entrez le Téléphone :").strip()
    email = input("Entrez l'email : ").strip().lower()
    ville = input("Entrez la ville :").strip().title()

    # Création d'un dictionnaire pour le contact
    nouveau_contact = {
        "nom": nom,
        "telephone": telephone,
        "email": email,
        "ville": ville
    }

    contacts.append(nouveau_contact)

    print(f"\nContact de {nom} ajouté avec succès !")

    sauvegarder_contacts()

# Afficher un contact
def afficher_contact():
    """Afficher tous les contacts."""
    if not contacts:
        print("\nAucun contact enregistré pour le moment.")
        return
    
    print("===Liste des contacts ===")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['nom']} - {contact['telephone']} - {contact['email']} - {contact['ville']}")

# Rechercher un contact
def rechercher_contact():
    """Recherche un contact par un nom ou par email"""
    if not contacts:
        print("\nAucun contact enregistré.")
        return
    
    recherche = input("\nEntrer le nom ou l'email à rechercher : ").strip()

    trouve = False

    for contact in contacts:
        # Recherche insensible à la casse.
        if(recherche.lower in contact['nom'].lower()) or recherche.lower() == contact['email'].lower():
           print("\n" +"="*40)
           print("✅ CONTACT TROUVE")
           print("="*40)
           print(f"Nom          : {contact['nom']}")
           print(f"Téléphone    : {contact['telephone']}")
           print(f"Email        : {contact['email']}")
           print(f"Ville        : {contact['ville']}")
           print("="*40)
           trouve = True
           # On continue la boucle pour afficher tous les résultats possibles

    if not trouve:
        print(f"\n❌ Aucun contact trouvé avec {recherche}")

# Modifier un contact
def modifier_contact():
    """Modifie les informations d'un contact existant"""

    if not contacts:
        print("\nAucun contact à modifier.")

    email_recherche = input("\nEntrez l'email du contact modifier :").strip().lower()

    for contact in contacts:
        if contact["email"] == email_recherche:
            print("\nContact trouvé. Quelles informations voulez-vous modifier ?")
            print("1. Nom")
            print("2. Téléphone")
            print("3. Email")
            print("4. Ville")
            print("5. Tout annuler")

            choix = input("\nVotre choix : ").strip()

            if choix == "1":
                contact["nom"] = input("Nouveau nom : ").strip().title()
            elif choix == "2":
                contact["telephone"] = input("Nouveau téléphone : ").strip().title()
            elif choix == "3":
                contact["email"] = input("Nouveau email : ").strip().title()
            elif choix == "4":
                contact["ville"] = input("Nouvelle ville : ").strip().title()
            elif choix == "5":
                print("Modification annulée")
                return
            else:
                print("Choix invalide.")
                return
            
            print(f"\n✅ Contact de {contact['nom']} modifié avec succès !")
            return
        
    print(f"\n❌ Aucun contact trouvé avec l'email : {email_recherche}")

    sauvegarder_contacts()
    
# Supprimer un contact
def supprimer_contact():
    """Supprime un contact par email"""
    if not contacts:
        print("\nAucun contact à supprimer")
        return
    
    email_recherche = input("\nEntrez l'email du contact à supprimer : ").strip().lower()

    for i, contact in enumerate(contacts):
        if contact['email'] == email_recherche:
            # Affichage des infos avant suppression
            print("\nContact trouvé :")
            print(f"Nom       : {contact['nom']}")
            print(f"Téléphone : {contact['telephone']}")
            print(f"Email     : {contact['email']}")
            print(f"Ville     : {contact['ville']}")

        # Confirmation
        confirmation = input("\nVoulez-vous vraiment supprimer ce contact ? (oui/non) : ").strip().lower()

        if confirmation == "oui":
            del contacts[i] # contacts.pop(i)
            print(f"\n ✅ Contact de {contact['nom']} supprimé avec succès !")
        else:
            print("\nSuppression annulée")
        
    print(f"\n❌ Aucun contact trouvé avec l'email : {email_recherche}")

    sauvegarder_contacts()

# Menu principal
while True:
    print("\n" + "="*50)
    print(Fore.CYAN + "\n    GESTIONNAIRE DE CONTACTS"  + Style.RESET_ALL)
    print("="*50)
    print(Fore.YELLOW + "1. Ajouter un contact")
    print(Fore.YELLOW + "2. Afficher tous les contacts")
    print(Fore.YELLOW + "3. Rechercher un contact")
    print(Fore.YELLOW + "4. Modifier un contact")
    print(Fore.YELLOW + "5. Supprimer un contact")
    print(Fore.YELLOW + "6. Quitter")
    print("="*50)

    choix = input(Fore.WHITE + "\nVotre choix : "   + Style.RESET_ALL).strip()

    if choix == "1":
        ajouter_contact()
    elif choix == "2":
        afficher_contact()
    elif choix == "3":
        rechercher_contact()
    elif choix == "4":
        modifier_contact()
    elif choix == "5":
        supprimer_contact()
    elif choix == "6":
        print(Fore.GREEN + "\n👋 Au revoir ! À bientôt." + Style.RESET_ALL)
        sauvegarder_contacts()
        break
    else:
        print(Fore.RED  + "\n❌ Choix invalide. Veuillez réessayer." + Style.RESET_ALL)