# MVC Project Sem 1, Geothermal Heat Flow
# Alice Su, Per. 2
# Dec 5, 2024

# Direction of Heat Flow, 2D Negative Gradient Field, Sized-Up (Fourier's Law of Heat Conduction)

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Dictionary to store city coordinates from Day 1
cities = {
    "San Francisco": (37.7749, -122.4194),
    "Pleasanton": (37.6624, -121.8747),
    "Livermore": (37.6819, -121.7680),
    "Dublin": (37.7022, -121.9358),
    "San Ramon": (37.7799, -121.9780),
    "Fremont": (37.5483, -121.9886),
    "San Jose": (37.3382, -121.8863),
    "Walnut Creek": (37.9101, -122.0652),
    "Palo Alto": (37.4419, -122.1430),
}

temps_day1 = [55, 57, 57, 57, 55, 58, 58, 55, 57]

# Extract latitude, longitude, and coordinates
latitudes = np.array([coord[0] for coord in cities.values()])
longitudes = np.array([coord[1] for coord in cities.values()])
coordinates = np.column_stack((latitudes, longitudes))

# Create a meshgrid for interpolation
lat_grid, lon_grid = np.meshgrid(
    np.linspace(latitudes.min(), latitudes.max(), 50),
    np.linspace(longitudes.min(), longitudes.max(), 50)
)

# Interpolate the temperature data
temperature_grid = griddata(coordinates, temps_day1, (lat_grid, lon_grid), method='cubic')

# Compute the gradient vectors 
grad_lat, grad_lon = np.gradient(temperature_grid)

# Define a function to plot the gradient field and save to file
def plot_gradient_field(lat_grid, lon_grid, grad_lat, grad_lon, title, output_path, scale=1.0):
    plt.figure(figsize=(10, 7))
    plt.quiver(
        lon_grid, lat_grid, grad_lon, grad_lat,
        color='blue', scale=scale, pivot='middle', width=0.003
    )
    plt.title(title)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid()
    # Save the plot to the specified file path
    plt.savefig(output_path, dpi=300)
    plt.close()

# Plot the gradient field with negative gradients
plot_gradient_field(
    lat_grid, lon_grid, -grad_lat, -grad_lon,
    title="Gradient Field of Day 1 Surface (Negative Gradients)",
    output_path="/Users/alicesu/Downloads/gradient_field_negative.png",
    scale=10
)

output_path

