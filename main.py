import random

# Fonction pour calculer la longueur d'un trajet
def calculer_longueur(trajet, dist_matrix):
    longueur = 0
    for i in range(len(trajet) - 1):
        longueur += dist_matrix[trajet[i]][trajet[i + 1]]
    longueur += dist_matrix[trajet[-1]][trajet[0]]  # Retour à la ville de départ   
    return longueur

# Fonction pour initialiser la population avec des trajets aléatoires
def initialiser_population(taille_population, num_villes):
    population = []
    for _ in range(taille_population):
        trajet = list(range(num_villes))
        random.shuffle(trajet)  # Mélange aléatoire des villes
        population.append(trajet)
    return population

# Fonction de croisement
def croisement(parent1, parent2):
    # Choisir un point de croisement
    point_croisement = random.randint(1, len(parent1) - 1)
    enfant1 = parent1[:point_croisement] + [ville for ville in parent2 if ville not in parent1[:point_croisement]]
    enfant2 = parent2[:point_croisement] + [ville for ville in parent1 if ville not in parent2[:point_croisement]]
    return enfant1, enfant2

# Fonction de mutation
def mutation(trajet, prob_mutation):
    if random.random() < prob_mutation:
        # Appliquer une mutation (échanger deux villes aléatoires)
        i, j = random.sample(range(len(trajet)), 2)
        trajet[i], trajet[j] = trajet[j], trajet[i]
    return trajet

# Fonction de sélection par tournoi
def selection_par_tournoi(population, dist_matrix):
    parents = []
    for _ in range(len(population) // 2):  # Assurez-vous que vous avez un nombre pair de parents
        tournoi = random.sample(population, 4)  # Choisir 4 individus aléatoires
        tournoi.sort(key=lambda x: calculer_longueur(x, dist_matrix))  # Trier par longueur
        parents.append(tournoi[0])  # Le meilleur individu du tournoi
    return parents

# Fonction de sélection par élitisme
def selection_par_elitisme(population, dist_matrix):
    population.sort(key=lambda x: calculer_longueur(x, dist_matrix))  # Trier par longueur
    return population[:len(population)//2]  # Garder la moitié des meilleurs individus

# Fonction principale de l'algorithme génétique
def tsp_genetic_algorithm(dist_matrix, population_size, generations, prob_mutation):
    num_villes = len(dist_matrix)
    population = initialiser_population(population_size, num_villes)
    meilleur_trajet = None
    meilleure_longueur = float('inf')

    for generation in range(generations):
        if generations % 2 == 0:  # Si le nombre de générations est pair, utiliser élitisme
            parents = selection_par_elitisme(population, dist_matrix)
        else:  # Si le nombre de générations est impair, utiliser tournoi
            parents = selection_par_tournoi(population, dist_matrix)

        # Assurez-vous que le nombre de parents est pair
        if len(parents) % 2 != 0:
            parents.append(random.choice(parents))  # Ajouter un parent aléatoire pour rendre la taille paire

        enfants = []

        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            enfant1, enfant2 = croisement(parent1, parent2)
            enfants.append(mutation(enfant1, prob_mutation))
            enfants.append(mutation(enfant2, prob_mutation))

        # Remplacer la population actuelle par la nouvelle génération
        population = parents + enfants

        # Sélectionner le meilleur trajet
        for individu in population:
            longueur = calculer_longueur(individu, dist_matrix)
            if longueur < meilleure_longueur:
                meilleur_trajet = individu
                meilleure_longueur = longueur

        print(f"Generation {generation + 1}: Meilleur trajet {meilleur_trajet}, distance = {meilleure_longueur} km")

    return meilleur_trajet, meilleure_longueur

# Fonction pour générer une matrice de distances aléatoires
def generer_distances(num_villes, min_distance=100, max_distance=1000):
    dist_matrix = [[0 if i == j else random.randint(min_distance, max_distance) for j in range(num_villes)] for i in range(num_villes)]
    
    # Rendre la matrice symétrique (distances entre i et j sont les mêmes que entre j et i)
    for i in range(num_villes):
        for j in range(i + 1, num_villes):
            dist_matrix[j][i] = dist_matrix[i][j]
    return dist_matrix

# Demande à l'utilisateur d'entrer des paramètres

def demander_entrées_utilisateur():
    try:
        population_size = int(input("Entrez la taille de la population (nombre d'individus) : "))
        if population_size <= 0:
            print("La taille de la population doit être un entier positif.")
            return demander_entrées_utilisateur()

        prob_mutation = float(input("Entrez la probabilité de mutation (entre 0 et 1) : "))
        if prob_mutation < 0 or prob_mutation > 1:
            print("La probabilité de mutation doit être entre 0 et 1.")
            return demander_entrées_utilisateur()

        generations = int(input("Entrez le nombre de générations : "))
        if generations <= 0:
            print("Le nombre de générations doit être un entier positif.")
            return demander_entrées_utilisateur()

        return population_size, prob_mutation, generations
    except ValueError:
        print("Entrée invalide. Veuillez entrer des valeurs numériques.")
        return demander_entrées_utilisateur()

# Exemple d'utilisation

# Liste des noms de villes en France
villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg"]

# Génération de la matrice de distances aléatoires entre les villes
dist_matrix = generer_distances(len(villes))

# Demande à l'utilisateur d'entrer la taille de la population, la probabilité de mutation et le nombre de générations
population_size, prob_mutation, generations = demander_entrées_utilisateur()

# Appel de l'algorithme génétique
best_route, best_length = tsp_genetic_algorithm(dist_matrix, population_size, generations, prob_mutation)

# Affichage du meilleur trajet et de sa longueur
meilleur_trajet_villes = [villes[i] for i in best_route]
print(f"\nMeilleur trajet final (villes) : {meilleur_trajet_villes}")
print(f"distance du meilleur trajet : {best_length} km")
