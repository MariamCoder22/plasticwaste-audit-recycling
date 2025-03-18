import numpy as np

class RouteOptimizer:
    def __init__(self, locations, pop_size=50, mutation_rate=0.01):
        self.locations = np.array(locations)
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate

    def _calculate_distance(self, route):
        return np.sum(np.linalg.norm(
            self.locations[route[:-1]] - self.locations[route[1:]], axis=1))

    def _mutate(self, route):
        if np.random.rand() < self.mutation_rate:
            i, j = sorted(np.random.choice(len(route), 2, replace=False))
            route[i:j] = route[i:j][::-1]
        return route

    def optimize(self, generations=1000):
        population = [np.random.permutation(len(self.locations)) 
                     for _ in range(self.pop_size)]
        
        for _ in range(generations):
            fitness = [1/self._calculate_distance(ind) for ind in population]
            parents = np.random.choice(
                population, size=self.pop_size, p=fitness/np.sum(fitness))
            
            new_pop = []
            for parent in parents:
                child = self._mutate(parent.copy())
                new_pop.append(child)
            
            population = new_pop
        
        return population[np.argmax([self._calculate_distance(ind) 
                                    for ind in population])]