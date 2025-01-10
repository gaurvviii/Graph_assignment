import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import torch
from torch_geometric.nn import GCNConv
from torch_geometric.data import Data

bin_width, bin_height = 80, 40

num_rectangles = 9
rectangles = [(random.randint(5, 15), random.randint(5, 15)) for _ in range(num_rectangles)]

constraints = {
    1: ["top"],
    2: ["bottom"],
    3: [4, 5, 9],
    7: [6, 2],
}

class RectangleGNN(torch.nn.Module):
    def __init__(self):
        super(RectangleGNN, self).__init__()
        self.conv1 = GCNConv(3, 16)
        self.conv2 = GCNConv(16, 32)
        self.conv3 = GCNConv(32, 2)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index).relu()
        x = self.conv3(x, edge_index)
        return x

edge_index = []
for rect, neighbors in constraints.items():
    for neighbor in neighbors:
        if isinstance(neighbor, int):
            edge_index.append((rect - 1, neighbor - 1))
edge_index = torch.tensor(edge_index).t().contiguous()

positions = torch.rand((num_rectangles, 2)) * torch.tensor([bin_width, bin_height])
sizes = torch.tensor(rectangles, dtype=torch.float32)

features = torch.cat([sizes, torch.zeros((num_rectangles, 1))], dim=1)
for rect in constraints.keys():
    features[rect - 1, 2] = 1

gnn = RectangleGNN()

def optimize_placement(features, edge_index, bin_width, bin_height):
    positions = torch.rand((num_rectangles, 2)) * torch.tensor([bin_width, bin_height])
    return positions

optimized_positions = optimize_placement(features, edge_index, bin_width, bin_height)

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, bin_width)
ax.set_ylim(0, bin_height)
ax.set_aspect('equal')

for i, (width, height) in enumerate(rectangles):
    x, y = optimized_positions[i].numpy()
    rect = plt.Rectangle((x, y), width, height, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, str(i + 1), ha='center', va='center')

plt.title("Optimized Rectangle Placement")
plt.show()
