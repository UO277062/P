# %% Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.datasets import ascent
from scipy.stats import norm

imagen = ascent().astype(float)

ruido = norm.rvs(loc=0, scale=16, size=imagen.shape, random_state=42)
imagen_ruido = np.clip(imagen + ruido, 0, 255)

#Imagen extra ejercicio1
ruido_extra = norm.rvs(loc=0, scale=64, size=imagen.shape, random_state=42)
imagen_extra = np.clip(imagen + ruido_extra, 0, 255)

# %% Celda 1
fig, ejes = plt.subplots(1, 3) # para mostrar 3 imagenes

ejes[0].imshow(imagen, cmap="gray", vmin=0, vmax=255)
ejes[0].set_title("Original")

ejes[1].imshow(imagen_ruido, cmap="gray", vmin=0, vmax=255)
ejes[1].set_title("Ruido: desviación 16")

# Añade la tercera imagen
ejes[2].imshow(imagen_extra, cmap="gray", vmin=0, vmax=255)
ejes[2].set_title("Ruido: desviación 64")


for eje in ejes:
    eje.axis("off")
plt.tight_layout()
plt.show()

