import imageio
import os
import matplotlib.pyplot as plt

def create_evolution_gif(output_path="results/evolution.gif"):
    images = []
    for file in sorted(os.listdir("results/plots")):
        if file.endswith(".png"):
            images.append(imageio.imread(f"results/plots/{file}"))
    imageio.mimsave(output_path, images, fps=5)