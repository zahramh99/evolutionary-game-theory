from src.core import SpatialGame, EvolutionaryAgent
from src.visualization import plot_cooperation_heatmap

def main():
    game = SpatialGame(size=50)
    agents = initialize_agents(100)  # Random strategies
    
    for gen in range(1000):
        game.play_round(agents)
        plot_cooperation_heatmap(game.grid, gen)
        agents = evolve_population(agents)
        
        if gen % 100 == 0:
            save_checkpoint(agents, f"results/checkpoints/gen_{gen}.pkl")

if __name__ == "__main__":
    main()