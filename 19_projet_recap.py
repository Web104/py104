# PROJET RECAPITULATIF

contacts = []

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
    """Recherche un contact par email"""
    
    email_recherche = input("\nEntrez l'email du contact à rechercher :").strip().lower()

    if not contacts:
        print("\nAucun contact enregistré.")
        return

    trouve = False
    for contact in contacts:
        if contact['email'] == email_recherche:
            print("\n✅ Contact trouvé !")
            print(f"Nom       : {contact['nom']}")
            print(f"Téléphone : {contact['telephone']}")
            print(f"Email     : {contact['email']}")
            print(f"Ville     : {contact['ville']}")
            trouve = True
            break
    if not trouve:
        print(f"\n❌ Aucun contact trouvé avec l'email : {email_recherche}")

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

# Menu principal
while True:
    print("\n" + "="*45)
    print("\n    GESTIONNAIRE DE CONTACTS")
    print("="*45)
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Modifier un contact")
    print("5. Supprimer un contact")
    print("6. Quitter")
    print("="*45)

    choix = input("\nVotre choix : ").strip()

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
        print("\n👋 Au revoir ! À bientôt.")
        break
    else:
        print("\n❌Choix invalide. Veuillez réessayer....")