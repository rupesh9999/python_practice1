import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the random walk
num_steps = 1000 # Number of steps in the walk
step_size = 1 # Distance per step

# Generate random steps: +1 or -1 for x and y directions
x_steps = np.random.choice([step_size, -step_size], size=num_steps)
y_steps = np.random.choice([step_size, -step_size], size=num_steps)

# Calculate cumulative positions (starting at origin: 0,0)
x_positions = np.cumsum(x_steps)
y_positions = np.cumsum(y_steps)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(x_positions, y_positions, color='blue', alpha=0.5, label='Molecualar Path')

# Mark the start and end points
plt.scatter(0, 0, color='green', s=100, label='Start') # Starting point
plt.scatter(x_positions[-1], y_positions[-1], color='red', s=100, label='End') # Ending point

# Add labels and title
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Molecular Motion: 2D Random walk')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

