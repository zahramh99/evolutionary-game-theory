from enum import Enum

class Strategy(Enum):
    TFT = "TitForTat" 
    PAVLOV = "WinStayLoseShift"
    RANDOM = "Random"

class EvolutionaryAgent:
    def __init__(self, strategy, mutation_rate=0.01):
        self.strategy = strategy
        self.mutation_rate = mutation_rate
        self.history = []
        
    def decide(self, opponent_history):
        """Strategy decision logic"""
        if self.strategy == Strategy.TFT:
            return opponent_history[-1] if opponent_history else 'C'
        elif self.strategy == Strategy.PAVLOV:
            return 'C' if len(set(opponent_history[-2:])) == 1 else 'D'
        else:
            return np.random.choice(['C','D'])