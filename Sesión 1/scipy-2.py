import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import uniform

x = np.linspace(1, 4, 1000)
fig, ejes = plt.subplots(1, 3)

# 1000 muestras de una distribución uniforme en [2,3]
muestras = uniform.rvs(size =1000, loc=2, scale=1)

# Funcion de densidad
ejes[0].plot(x, uniform.pdf(x,loc=2, scale=1))
ejes[0].set_title("Densidad")

# Funcion de distribución
ejes[1].plot(x, uniform.cdf(x, loc=2, scale=1))
ejes[1].set_title("Distribución")

ejes[2].plot(muestras)
ejes[2].set_title("1000 muestras")

plt.tight_layout()
plt.show()



