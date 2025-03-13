#Nom : Sow Prenom : Mamadou Dian : Dep L3 info
import csv
import json  # Utilisé pour sauvegarder la liste sous forme de fichier JSON

def lire_csv(nom_fichier):
    """Lit le fichier CSV et retourne les données sous forme de liste de dictionnaires."""
    donnees = []
    with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            try:
                # Conversion des valeurs numériques en entiers
                ligne['Cas'] = int(ligne['Cas'])
                ligne['Deces'] = int(ligne['Deces'])
            except (ValueError, KeyError):
                # Gestion des erreurs si des données sont manquantes ou mal formatées
                print(f"Erreur de conversion pour la ligne : {ligne}")
                continue
            donnees.append(ligne)
    return donnees

def sauvegarder_donnees(donnees, nom_fichier_sauvegarde):
    """Sauvegarde les données sous forme de liste de dictionnaires dans un fichier JSON."""
    with open(nom_fichier_sauvegarde, mode='w', encoding='utf-8') as fichier:
        json.dump(donnees, fichier, ensure_ascii=False, indent=4)
    print(f"Données sauvegardées dans {nom_fichier_sauvegarde}")

# Utilisation des fonctions
donnees = lire_csv('ebola_guinea.csv')
sauvegarder_donnees(donnees, 'sauve.json')
