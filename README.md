# Black Hole Model

## Agujero Negro
Un agujero negro es una región del espacio-tiempo donde la gravedad es tan intensa que nada, ni siquiera la luz, puede escapar de él. Se forma cuando una estrella colapsa bajo su propia gravedad al final de su vida, o por otros mecanismos como la fusión de agujeros negros más pequeños. 
![black-hole](/img/black-hole.jpg)
La superficie de un agujero negro, conocida como el horizonte de eventos, marca el límite más allá del cual la atracción gravitatoria es tan fuerte que no hay retorno.
![black-hole-about](/img/black-hole-about.jpg)
### Librerias Usadas
Numpy se usa para operaciones numéricas y matplotlib.pyplot junto con mpl_toolkits.mplot3d se usa para la visualización en 3D.
```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```
Imagen Generada al ejecutar el script.
![black-hole-model](/img/black-hole-model.jpg)
### Horizonte de Eventos
El horizonte de eventos es la "frontera" alrededor de un agujero negro más allá de la cual nada puede escapar. Es una especie de "línea sin retorno". Una vez que un objeto cruza este límite, no puede volver a salir del agujero negro, y la información sobre el objeto se pierde para el exterior.
```python
r_event_horizon = 1.0  # Radio del horizonte de eventos
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = r_event_horizon * np.sin(theta) * np.cos(phi)
y = r_event_horizon * np.sin(theta) * np.sin(phi)
z = r_event_horizon * np.cos(theta)
ax.plot_surface(x, y, z, color='black', alpha=1.0)
```
* Radio: r_event_horizon define el radio del horizonte de eventos del agujero negro.
* Ángulos: theta y phi son las coordenadas esféricas.
* Malla de coordenadas: np.meshgrid genera matrices bidimensionales para theta y phi.
* Coordenadas cartesianas: Se calculan x, y, z usando coordenadas esféricas.
* Dibujo: ax.plot_surface dibuja la esfera negra que representa el horizonte de eventos del agujero negro.
### Ergosfera
La ergosfera es una región que se encuentra fuera del horizonte de eventos en los agujeros negros rotatorios (a veces llamados agujeros negros de Kerr). En esta región, el espacio-tiempo está en rotación junto con el agujero negro. Los objetos en la ergosfera pueden ser arrastrados en esta rotación, y es aquí donde se puede extraer energía del agujero negro a través del proceso conocido como el mecanismo de Penrose.
```python
r_ergosphere = 1.5  # Radio de la ergosfera
x_ergosphere = r_ergosphere * np.sin(theta) * np.cos(phi)
y_ergosphere = r_ergosphere * np.sin(theta) * np.sin(phi)
z_ergosphere = r_ergosphere * np.cos(theta)
ax.plot_surface(x_ergosphere, y_ergosphere, z_ergosphere, color='gray', alpha=0.3)
```
* Radio: r_ergosphere define el radio de la ergosfera, que es una región exterior al horizonte de eventos donde el espacio-tiempo está distorsionado.
* Coordenadas: x_ergosphere, y_ergosphere, z_ergosphere se calculan de manera similar a las del horizonte de eventos, pero con un radio mayor.
* Dibujo: ax.plot_surface dibuja la ergosfera como una esfera gris translúcida.
### Disco de Acreción
El disco de acreción es un disco de materia que gira alrededor de un agujero negro, formado por material que cae hacia él. A medida que la materia en el disco se acerca al agujero negro, se calienta debido a la fricción y la compresión, emitiendo radiación en una variedad de longitudes de onda, incluyendo rayos X. Este disco es muy brillante y es una de las principales fuentes de radiación detectable desde agujeros negros.
```python
r_accretion_disk = np.linspace(1.0, 2.5, 100)
theta_disk = np.linspace(0, 2 * np.pi, 100)
r_accretion_disk, theta_disk = np.meshgrid(r_accretion_disk, theta_disk)
x_disk = r_accretion_disk * np.cos(theta_disk)
y_disk = r_accretion_disk * np.sin(theta_disk)
z_disk = np.zeros_like(x_disk)
ax.plot_surface(x_disk, y_disk, z_disk, color='orange', alpha=0.5)
```
* Radios y ángulos: r_accretion_disk y theta_disk definen el rango radial y angular del disco de acreción.
* Malla de coordenadas: np.meshgrid se usa para generar las matrices de coordenadas radiales y angulares.
* Coordenadas cartesianas: x_disk, y_disk, z_disk se calculan para formar un disco plano en el eje z.
### Chorro Relativista
Los chorros relativistas son flujos de partículas muy energéticas que son expulsadas a lo largo del eje de rotación de algunos agujeros negros. Estos chorros son lanzados a velocidades cercanas a la velocidad de la luz y son el resultado de la interacción entre el campo magnético del agujero negro y el material en el disco de acreción. Los chorros pueden extenderse a distancias extremadamente largas desde el agujero negro y son observables en diferentes longitudes de onda, como radio y rayos X.
```python
z_jet = np.linspace(-3, 3, 100)
r_jet = 0.1  # Radio del chorro
theta_jet = np.linspace(0, 2 * np.pi, 50)
z_jet, theta_jet = np.meshgrid(z_jet, theta_jet)
x_jet = r_jet * np.cos(theta_jet)
y_jet = r_jet * np.sin(theta_jet)
ax.plot_surface(x_jet, y_jet, z_jet, color='blue', alpha=0.7)
```
* Z: z_jet define la extensión vertical de los chorros relativistas.
* Radio: r_jet define el radio de los chorros.
* Ángulo: theta_jet es el ángulo angular alrededor del eje z.
* Malla de coordenadas: np.meshgrid crea matrices bidimensionales para z_jet y theta_jet.
* Coordenadas cartesianas: x_jet, y_jet se calculan para formar cilindros que representan los chorros relativistas.
* Dibujo: ax.plot_surface dibuja los chorros como cilindros azules semitransparentes.

### Configuración Final
```python
# Configuración de los ejes
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title("Balck Hole Model")

plt.show()
```
* Rango de ejes: ax.set_xlim, ax.set_ylim, ax.set_zlim establecen los límites de los ejes x, y, z.
* Etiquetas: ax.set_xlabel, ax.set_ylabel, ax.set_zlabel etiquetan los ejes.
* Título: ax.set_title añade un título al gráfico.
* Mostrar gráfico: plt.show() renderiza la visualización.
