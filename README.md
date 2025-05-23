# Evolutionary Game Theory Simulation

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features
- Spatial Prisoner's Dilemma simulations
- Multiple strategy implementations (TFT, Pavlov, etc.)
- Genetic algorithm-based evolution
- Real-time visualization

## Quick Start
```bash
git clone https://github.com/zahramh99/evolutionary-game-theory.git
cd evolutionary-game-theory
pip install -r requirements.txt
python src/main.py

## **5. Key Extensions for Research**  

1. **RL Strategy Optimization**  
   ```python
   class RLAgent(EvolutionaryAgent):
       def __init__(self):
           super().__init__()
           self.q_table = defaultdict(lambda: np.random.uniform(0,1,2))  # Q-learning