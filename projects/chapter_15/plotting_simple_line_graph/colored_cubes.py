import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data points for a 5*5*5 grid of cubes
n = 5
x, y, z = np.indices((n, n, n))

# Flatten the arrays to create a list of cube vertices
x = x.flatten()
y = y.flatten()
z = z.flatten()

# Use z-values to determine colors (normalized between 0 and 1)
colors = z / n

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the cubes (using scatter with larger markers to simulate cubes)
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=100, marker='s')

# Add a colorbar to show the mapping of z-values to colors
fig.colorbar(scatter, ax=ax, label='Z value')

# Set labels for the axes
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set the title
ax.set_title('3D Colored Cubes')

# Show the plot
plt.show()