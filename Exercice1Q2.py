#Nom : Sow Prenom : Mamadou Dian : Dep L3 info
import csv
import matplotlib.pyplot as plt

def lire_csv(nom_fichier):
    """Lit le fichier CSV et retourne les données sous forme de liste de dictionnaires."""
    donnees = []
    with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for ligne in lecteur:
            # Conversion des valeurs numériques en entiers
            ligne['Cas'] = int(ligne['Cas'])
            ligne['Deces'] = int(ligne['Deces'])
            donnees.append(ligne)
    return donnees

def calcul_statistiques(donnees):
    """Calcule le total des cas, des décès et le taux de mortalité par préfecture."""
    stats = {}
    for ligne in donnees:
        prefecture = ligne['Prefecture']
        cas = ligne['Cas']
        deces = ligne['Deces']

        if prefecture not in stats:
            stats[prefecture] = {'total_cas': 0, 'total_deces': 0}

        stats[prefecture]['total_cas'] += cas
        stats[prefecture]['total_deces'] += deces

    # Calcul du taux de mortalité
    for prefecture in stats:
        total_cas = stats[prefecture]['total_cas']
        total_deces = stats[prefecture]['total_deces']
        stats[prefecture]['taux_mortalite'] = total_deces / total_cas if total_cas else 0

    return stats

def visualiser_statistiques(stats):
    """Crée des visualisations des statistiques calculées."""
    prefectures = list(stats.keys())
    total_cas = [stats[p]['total_cas'] for p in prefectures]
    taux_mortalite = [stats[p]['taux_mortalite'] for p in prefectures]

    # Diagramme à barres pour le nombre total de cas
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, total_cas, color='skyblue')
    plt.title('Nombre Total de Cas par Préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Nombre de Cas')
    plt.show()

    # Diagramme à barres pour le taux de mortalité
    plt.figure(figsize=(10, 5))
    plt.bar(prefectures, taux_mortalite, color='salmon')
    plt.title('Taux de Mortalité par Préfecture')
    plt.xlabel('Préfecture')
    plt.ylabel('Taux de Mortalité')
    plt.show()

def main():
    nom_fichier = 'ebola_guinea.csv'
    donnees = lire_csv(nom_fichier)
    stats = calcul_statistiques(donnees)
    visualiser_statistiques(stats)

if __name__ == '__main__':
    main()
