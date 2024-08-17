import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Horizonte de eventos (esfera negra)
r_event_horizon = 1.0  # Radio del horizonte de eventos
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = r_event_horizon * np.sin(theta) * np.cos(phi)
y = r_event_horizon * np.sin(theta) * np.sin(phi)
z = r_event_horizon * np.cos(theta)
ax.plot_surface(x, y, z, color='black', alpha=1.0)

# Ergosfera (esfera más grande)
r_ergosphere = 1.5  # Radio de la ergosfera
x_ergosphere = r_ergosphere * np.sin(theta) * np.cos(phi)
y_ergosphere = r_ergosphere * np.sin(theta) * np.sin(phi)
z_ergosphere = r_ergosphere * np.cos(theta)
ax.plot_surface(x_ergosphere, y_ergosphere, z_ergosphere, color='gray', alpha=0.3)

# Disco de acreción (disco alrededor del horizonte de eventos)
r_accretion_disk = np.linspace(1.0, 2.5, 100)
theta_disk = np.linspace(0, 2 * np.pi, 100)
r_accretion_disk, theta_disk = np.meshgrid(r_accretion_disk, theta_disk)
x_disk = r_accretion_disk * np.cos(theta_disk)
y_disk = r_accretion_disk * np.sin(theta_disk)
z_disk = np.zeros_like(x_disk)
ax.plot_surface(x_disk, y_disk, z_disk, color='orange', alpha=0.5)

# Chorro relativista (jets)
z_jet = np.linspace(-3, 3, 100)
r_jet = 0.1  # Radio del chorro
theta_jet = np.linspace(0, 2 * np.pi, 50)
z_jet, theta_jet = np.meshgrid(z_jet, theta_jet)
x_jet = r_jet * np.cos(theta_jet)
y_jet = r_jet * np.sin(theta_jet)
ax.plot_surface(x_jet, y_jet, z_jet, color='blue', alpha=0.7)

# Configuración de los ejes
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title("Black Hole Model")

plt.show()
