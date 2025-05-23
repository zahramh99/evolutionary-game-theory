def evolve_population(population, elitism=0.2):
    """Genetic algorithm implementation"""
    sorted_pop = sorted(population, key=lambda x: x.score, reverse=True)
    
    # Elite selection
    elites = sorted_pop[:int(elitism*len(population))]
    
    # Tournament selection
    offspring = []
    while len(offspring) < len(population) - len(elites):
        parents = np.random.choice(sorted_pop[:len(population)//2], 2, replace=False)
        child = crossover(parents[0], parents[1])
        offspring.append(mutate(child))
    
    return elites + offspring

def crossover(parent1, parent2):
    """Uniform crossover"""
    child_strategy = parent1.strategy if np.random.rand() > 0.5 else parent2.strategy
    return EvolutionaryAgent(strategy=child_strategy)