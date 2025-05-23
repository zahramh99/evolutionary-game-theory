import numpy as np

class SpatialGame:
    def __init__(self, size=50, topology="grid"):
        """Initialize spatial game environment"""
        self.size = size
        self.grid = self._init_topology(topology)
        self.payoffs = {
            ('C','C'): (3,3), 
            ('C','D'): (0,5),
            ('D','C'): (5,0),
            ('D','D'): (1,1)
        }
    
    def _init_topology(self, topology):
        """Create network structure"""
        if topology == "grid":
            return np.zeros((self.size, self.size))
        elif topology == "small_world":
            return nx.watts_strogatz_graph(self.size**2, k=4, p=0.1)
    
    def play_round(self):
        """Execute one generation of gameplay"""
        for i, j in np.ndindex(self.grid.shape):
            neighbors = self._get_neighbors(i,j)
            payoffs = [self.payoffs[(self.grid[i,j], self.grid[n])] for n in neighbors]
            self.scores[i,j] = sum(p for p,_ in payoffs)