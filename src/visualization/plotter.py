import matplotlib.pyplot as plt

def plot_cooperation_heatmap(grid, generation):
    plt.imshow(grid == 'C', cmap='RdYlGn')
    plt.title(f"Generation {generation}")
    plt.savefig(f"results/plots/gen_{generation}.png")