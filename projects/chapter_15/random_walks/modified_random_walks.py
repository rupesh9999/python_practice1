import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the random walk
num_steps = 1000  # Number of steps in the walk
max_step_size = 4  # Maximum distance per step

# Generate random angles (0 to 2π) and step sizes (0 to max_step_size)
angles = np.random.uniform(0, 2 * np.pi, size=num_steps)  # Random angles in radians
step_sizes = np.random.uniform(0, max_step_size, size=num_steps)  # Random step distances

# Calculate x and y step components using trigonometry
x_steps = step_sizes * np.cos(angles)  # x = r * cos(θ)
y_steps = step_sizes * np.sin(angles)  # y = r * sin(θ)

# Calculate cumulative positions (starting at origin: 0,0)
x_positions = np.cumsum(x_steps)
y_positions = np.cumsum(y_steps)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, color='purple', alpha=0.5, label='Modified Walk')

# Mark the start and end points
plt.scatter(0, 0, color='green', s=100, label='Start')  # Starting point
plt.scatter(x_positions[-1], y_positions[-1], color='red', s=100, label='End')  # End point

# Add labels, title, and legend
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Modified Random Walk: Variable Directions and Distances')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()