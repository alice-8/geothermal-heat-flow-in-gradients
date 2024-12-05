# MVC Project Sem 1, Geothermal Heat Flow
# Alice Su, Per. 2
# Dec 4, 2024

# Direction of Heat Flow, 2D Gradient Field Final Product


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import griddata

# City coordinates (latitude, longitude)
cities = {
    "San Francisco": (37.7749, -122.4194),
    "Pleasanton": (37.6624, -121.8747),
    "Livermore": (37.6819, -121.7680),
    "Dublin": (37.7022, -121.9358),
    "San Ramon": (37.7799, -121.9780),
    "Fremont": (37.5483, -121.9886),
    "San Jose": (37.3382, -121.8863),
    "Walnut Creek": (37.9101, -122.0652),
    "Palo Alto": (37.4419, -122.1430)
}

# Temperatures for four days
temperatures = {
    "Day 1": [55, 57, 57, 57, 55, 58, 58, 55, 57],
    "Day 2": [56, 56, 56, 56, 56, 57, 57, 57, 57],
    "Day 3": [55, 56, 55, 56, 55, 57, 56, 55, 56],
    "Day 4": [57, 57, 56, 57, 57, 58, 58, 56, 57]
}

# Extract coordinates and organize data
latitudes = np.array([coord[0] for coord in cities.values()])
longitudes = np.array([coord[1] for coord in cities.values()])
coordinates = np.column_stack((latitudes, longitudes))

# Create a meshgrid
lat_grid, lon_grid = np.meshgrid(
    np.linspace(latitudes.min(), latitudes.max(), 50),
    np.linspace(longitudes.min(), longitudes.max(), 50)
)

# Function to interpolate temperatures
def interpolate_temps(coords, temps, lat_grid, lon_grid):
    grid_temps = griddata(coords, temps, (lat_grid, lon_grid), method='cubic')
    return grid_temps

# Prepare temperature grids for each day
temperature_grids = []
for day, temps in temperatures.items():
    temp_grid = interpolate_temps(coordinates, temps, lat_grid, lon_grid)
    temperature_grids.append(temp_grid)

# Calculate gradient fields for each day
gradient_fields = []
for grid in temperature_grids:
    grad_y, grad_x = np.gradient(grid)
    gradient_fields.append((grad_x, grad_y))

# Set up the figure
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(latitudes.min(), latitudes.max())
ax.set_ylim(longitudes.min(), longitudes.max())

# Initialize quiver plot
quiver = ax.quiver(lat_grid, lon_grid, gradient_fields[0][0], gradient_fields[0][1])

# Function to update the plot
def update(frame):
    ax.clear()
    ax.set_title(f"Temperature Gradient Field: {list(temperatures.keys())[frame]}")
    ax.set_xlabel("Latitude")
    ax.set_ylabel("Longitude")
    quiver = ax.quiver(lat_grid, lon_grid, 
                       gradient_fields[frame][0], gradient_fields[frame][1], 
                       scale=50, color="blue")
    return quiver,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(gradient_fields), interval=1000, blit=False)

# Save as GIF
output_path = "/Users/alicesu/Downloads/temperature_gradient_field_animation.gif"
ani.save(output_path, writer="imagemagick", fps=1)
output_path
