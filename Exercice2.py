#Nom : Sow Prenom : Mamadou Dian : Dep L3 info
#Importation de la bibliotheque random

import random


class Personne:
    """
    Classe représentant une personne.
    """

    def __init__(self, nom, proba_infection):
        """Initialise une personne saine avec une probabilité d'infection."""
        self.nom = nom
        self.sante = "saine"
        self.proba_infection = proba_infection

    def infecter(self):
        """Change l'état de santé en 'infectee'."""
        self.sante = "infectee"

    def immuniser(self):
        """Change l'état de santé en 'immunisee'."""
        self.sante = "immunisee"

    def __str__(self):
        """Retourne une représentation de la personne (nom et état de santé)."""
        return f"Nom: {self.nom}, Santé: {self.sante}"


class Population:

    """
    Classe représentant une population d'individus.
    """

    def __init__(self, taille_population, proba_infection):
        """Crée une population de taille donnée avec une probabilité d'infection donnée."""
        self.individus = [Personne(f"Personne_{i + 1}", proba_infection) for i in range(taille_population)]

    def introduire_infection(self, nombre_infectes):
        """Infecte un nombre donné d'individus choisis aléatoirement."""
        infectes = random.sample(self.individus, nombre_infectes)
        for individu in infectes:
            individu.infecter()

    def simuler_jour(self, proba_guerison):
        """
        Simule une journée de propagation de la maladie.
        - Les personnes infectées peuvent guérir.
        - Les personnes saines peuvent être infectées si elles croisent des infectées.
        """
        # Étape 1: Guérison des personnes infectées
        for individu in self.individus:
            if individu.sante == "infectee" and random.random() < proba_guerison:
                individu.immuniser()

        # Étape 2: Propagation de la maladie
        infectes = [ind for ind in self.individus if ind.sante == "infectee"]
        for individu in self.individus:
            if individu.sante == "saine":
                # Si en contact avec au moins un infecté
                if any(random.random() < individu.proba_infection for _ in infectes):
                    individu.infecter()

    def __str__(self):
        """Retourne un résumé de l'état de la population."""
        saines = sum(1 for ind in self.individus if ind.sante == "saine")
        infectees = sum(1 for ind in self.individus if ind.sante == "infectee")
        immunisees = sum(1 for ind in self.individus if ind.sante == "immunisee")
        return f"Saines: {saines}, Infectées: {infectees}, Immunisées: {immunisees}"


# ----------------- Simulation ----------------- #

def simulation():
    # 1. Créer une population de 1000 personnes avec une probabilité d'infection de 0.1
    population = Population(taille_population=1000, proba_infection=0.1)

    # 2. Introduire initialement 10 personnes infectées
    population.introduire_infection(nombre_infectes=10)

    # 3. Simuler 30 jours de propagation avec une probabilité de guérison de 0.05
    for jour in range(1, 31):
        print(f"\n--- Jour {jour} ---")
        population.simuler_jour(proba_guerison=0.05)
        print(population)


# Lancer la simulation
if __name__ == "__main__":
    simulation()
