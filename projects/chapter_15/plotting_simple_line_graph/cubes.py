import matplotlib.pyplot as plt

# Define input values and calculate cubes
input_values = [1, 2, 3, 4, 5]
cubes = [x**3 for x in input_values] # Calcualtes [1^3, 2^3, 3^3, 4^3, 5^3] = [1, 8, 27, 64, 125]

# Apply plot style
plt.style.use('seaborn-v0_8')

# Create figure and axes
fig, ax = plt.subplots()

# Plot the cubes as a line plot
ax.plot(input_values, cubes, linewidth=3)

# Set chart title and label axes
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

# Set size od tick labels
ax.tick_params(axis='both', labelsize=14)

# Display the plot
plt.show()