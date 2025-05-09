import matplotlib.pyplot as plt
import numpy as np

class RandomWalk:
    """A class to generate a random walk."""
    
    def __init__(self, num_steps=1000, step_size=1):
        """Initialize random walk attributes."""
        self.num_steps = num_steps  # Number of steps
        self.step_size = step_size  # Fixed step size
        # Starting point
        self.x_positions = [0]
        self.y_positions = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Generate steps until we reach desired number
        while len(self.x_positions) < self.num_steps:
            # Decide direction: +1 or -1 for x and y
            x_step = np.random.choice([self.step_size, -self.step_size])
            y_step = np.random.choice([self.step_size, -self.step_size])
            
            # Ignore steps that go nowhere (both x and y are 0)
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate new position
            new_x = self.x_positions[-1] + x_step
            new_y = self.y_positions[-1] + y_step
            
            # Add new position to the lists
            self.x_positions.append(new_x)
            self.y_positions.append(new_y)

# Create and fill a random walk
rw = RandomWalk(num_steps=1000, step_size=1)
rw.fill_walk()

# Plot the walk
plt.figure(figsize=(8, 8))
plt.plot(rw.x_positions, rw.y_positions, color='blue', alpha=0.5, label='Random Walk')

# Mark the start and end points
plt.scatter(0, 0, color='green', s=100, label='Start')  # Starting point
plt.scatter(rw.x_positions[-1], rw.y_positions[-1], color='red', s=100, label='End')  # End point

# Add labels, title, and legend
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Refactored Random Walk')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()