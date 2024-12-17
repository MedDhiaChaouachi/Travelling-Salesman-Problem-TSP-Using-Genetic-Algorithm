# Travelling Salesman Problem (TSP) Using Genetic Algorithm

This project implements a Genetic Algorithm to solve the **Travelling Salesman Problem (TSP)**. The TSP is a classic optimization problem where the goal is to find the shortest possible route that visits a given set of cities exactly once and returns to the origin city.

## Features

- **Random Distance Matrix**: Generate a random symmetric distance matrix for cities.
- **Genetic Algorithm Components**:
  - Population Initialization
  - Crossover for generating offspring
  - Mutation for diversity
  - Selection mechanisms: Tournament and Elitism
- **Dynamic Parameters**:
  - Population size
  - Mutation probability
  - Number of generations
- **Interactive Input**: Users can input parameters such as population size, mutation probability, and number of generations.
- **Cities Representation**: Includes predefined city names (e.g., Paris, Marseille, Lyon).

## How It Works

1. **Input Parameters**: Users provide population size, mutation probability, and number of generations.
2. **Distance Matrix**: A symmetric random matrix is generated to represent distances between cities.
3. **Genetic Algorithm Execution**:
   - **Initialization**: Random routes are created.
   - **Selection**: Uses Tournament or Elitism methods alternately based on the generation number.
   - **Crossover**: Combines parent routes to produce offspring.
   - **Mutation**: Randomly swaps cities in a route to explore new solutions.
4. **Output**: The best route and its total distance are displayed for each generation.

## Requirements

- Python 3.6+
- No external libraries required (uses Python's built-in libraries such as `random`).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/TSP-Genetic-Algorithm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TSP-Genetic-Algorithm
   ```
3. Run the Python script:
   ```bash
   python tsp_genetic_algorithm.py
   ```

## Usage

1. Run the script and input the required parameters when prompted:
   - **Population Size**: Number of individuals in the population.
   - **Mutation Probability**: Probability of mutation for a route.
   - **Number of Generations**: Total number of iterations.
2. Observe the best route and its total distance after each generation.
3. View the final optimal route and its distance.


### Input
```
Entrez la taille de la population (nombre d'individus) : 50
Entrez la probabilité de mutation (entre 0 et 1) : 0.2
Entrez le nombre de générations : 100
```

### Output
```
Generation 1: Meilleur trajet [2, 5, 3, 1, 4, 0, 6], distance = 2950 km
...
Meilleur trajet final (villes) : ['Lyon', 'Nantes', 'Toulouse', 'Marseille', 'Nice', 'Paris', 'Strasbourg']
distance du meilleur trajet : 2100 km
```


## License
feal free to use 
