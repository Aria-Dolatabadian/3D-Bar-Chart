import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [40, 30, 25, 25]  # Values for each category
explode = [0.1, 0.1, 0.1, 0.1]  # Explode out each slice for better visibility
colors = ['gold', 'lightblue', 'lightgreen', 'pink']  # Custom slice colors

# Create 3D Chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 3D effect through heights
theta = np.linspace(0, 2 * np.pi, len(sizes) + 1)
radii = np.cumsum([0] + sizes) / sum(sizes)  # Cumulative sizes for slice proportions
heights = np.linspace(0.05, 0.2, len(sizes))  # Varying heights for slices

for i, size in enumerate(sizes):
    ax.bar3d(
        x=[0],  # X position (0 for chart)
        y=[0],  # Y position (0 for chart)
        z=[heights[i]],  # Start height of the slice
        dx=[np.sin(theta[i + 1]) - np.sin(theta[i])],  # Width of slice
        dy=[np.cos(theta[i + 1]) - np.cos(theta[i])],  # Depth of slice
        dz=[size],  # Height based on the value
        color=colors[i],
        alpha=0.8
    )

# Add labels
plt.legend(labels, loc="upper left")
ax.set_title("3D Chart")
plt.show()



