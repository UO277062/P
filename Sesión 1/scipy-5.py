import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import minkowski

rejilla = np.meshgrid(
    np.linspace(-1.1, 1.1, 512),
    np.linspace(-1.1, 1.1, 512),
    indexing="ij",
)

X, Y = rejilla

# Función que decide si un punto está dentro de la bola. Calcula la distancia de Minkowski de orden p entre el punto (x, y) y el origen (0, 0)
def en_bola(x, y, p):
    return minkowski([x, y], [0, 0], p) <= 1

def bola(p):
    return np.vectorize(en_bola)(X, Y, p)

# Valores de p a mostrar: Manhattan(1), Euclídea(2), Minkowski(4), Chebyshev(inf)
valores_p = [1, 2, 4, np.inf]
titulos = ["Manhattan (p=1)", "Euclídea (p=2)", "Minkowski (p=4)", "Chebyshev (p=inf)"]

fig, ejes = plt.subplots(1, 4, figsize=(12, 3))

for i in range(len(valores_p)):
    ejes[i].imshow(
        bola(valores_p[i]),
        extent=[-1.1, 1.1, -1.1, 1.1],
        origin="lower",
        cmap="Blues",
    )
    ejes[i].set_title(titulos[i])
    ejes[i].set_aspect("equal")
    ejes[i].axis("off")

plt.tight_layout()
plt.show()