import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_1samp, wilcoxon

derecha = np.array([
    113, 105, 130, 101, 138, 118, 87, 116, 75, 96,
    122, 103, 116, 107, 118, 103, 111, 104, 111, 89,
    78, 100, 89, 85, 88,
])
izquierda = np.array([
    137, 105, 133, 108, 115, 170, 103, 145, 78, 107,
    84, 148, 147, 87, 166, 146, 123, 135, 112, 93,
    76, 116, 78, 101, 123,
])

diferencias = izquierda - derecha
print("Media:", diferencias.mean())
print("Desviación típica muestral:", diferencias.std(ddof=1))

plt.hist(diferencias, edgecolor="white")
plt.xlabel("Diferencia: izquierda - derecha (s)")
plt.ylabel("Frecuencia")
plt.show()

#  contraste t 
resultado = ttest_1samp(diferencias, popmean=0)
print(f"t = {resultado.statistic:.3f}; p = {resultado.pvalue:.4f}")
if resultado.pvalue < 0.05:
    print("Rechazamos H0: hay evidencia de una diferencia media.")
else:
    print("No rechazamos H0: la evidencia no es suficiente.")

#  contraste wilcoxon 
resultado_w = wilcoxon(diferencias)
print(f"Wilcoxon: estadístico = {resultado_w.statistic:.3f}; p = {resultado_w.pvalue:.4f}")

if resultado_w.pvalue < 0.05:
    print("Rechazamos H0: hay evidencia de una diferencia entre las medianas.")
else:
    print("No rechazamos H0: la evidencia no es suficiente.")



