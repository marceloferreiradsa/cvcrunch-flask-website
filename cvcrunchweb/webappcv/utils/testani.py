import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Parameters
Z = 100  # Number of subjects
positions = np.random.rand(Z, 2)  # Random positions of subjects in a 2D space

# Circle status: 0 for white, 1 for green, 2 for red
status = np.zeros(Z)

# Sensitivity thresholds
thresholds = np.random.rand(Z)  # Random sensitivity thresholds

def apply_action():
    """Apply actions to randomly selected circles."""
    good_circle = random.randint(0, Z-1)
    bad_circle = random.randint(0, Z-1)

    # Apply good action
    if status[good_circle] == 0:
        w = random.random()
        if w > thresholds[good_circle]:
            status[good_circle] = 1
            affect_neighbors(good_circle, 1)

    # Apply bad action
    if status[bad_circle] == 0:
        w = random.random()
        if w > thresholds[bad_circle]:
            status[bad_circle] = 2
            affect_neighbors(bad_circle, 2)

def affect_neighbors(circle_index, new_status):
    """Affect neighbors of a circle based on an action."""
    for i in range(Z):
        if i != circle_index and np.linalg.norm(positions[i] - positions[circle_index]) < 0.1:
            if status[i] == 0:  # Affect only white circles
                status[i] = new_status

def update(frame):
    """Update function for the animation."""
    apply_action()
    scatter.set_array(status)
    return scatter,

# Set up the plot
fig, ax = plt.subplots()
scatter = ax.scatter(positions[:, 0], positions[:, 1], c=status, cmap='viridis', s=100)
ax.axis('off')

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(300), interval=100, blit=True, repeat=False)

plt.show()
