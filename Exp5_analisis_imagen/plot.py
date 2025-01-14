"""Graficación de los valores de irradiancia de las imagenes de prueba (práctica 5a)"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo Excel
df = pd.read_excel("Exp5_analisis_imagen/roiStats.xlsx")
# df = pd.read_excel("Exp5_analisis_imagen/pixelIrradiance.xlsx")

# Extraer columnas como arrays de NumPy
# errors = [df["Rstd"].to_numpy()]

# Angulos
angles = np.arange(0, 360 + 1, 10)
angles = angles * np.pi / 180

# Crear la figura y los ejes polares
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
# fig, ax = plt.subplots()

# Formato de las gráficas
format_plot = dict(marker="o", ls="-", lw="0.5", fillstyle="none")
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# Gráfica de los puntos con barras de error radiales
ax.plot(
    angles,
    df["Rmean"].to_numpy(),
    label="Irradiancia Roja",
    color=colors["red"],
    **format_plot
)
ax.plot(
    angles,
    df["Gmean"].to_numpy(),
    label="Irradiancia Verde",
    color=colors["green"],
    **format_plot
)
ax.plot(
    angles,
    df["Bmean"].to_numpy(),
    label="Irradiancia Azul",
    color=colors["blue"],
    **format_plot
)

# ax.errorbar(
#     angles,
#     radii,
#     yerr=errors,
#     fmt=".",
#     color="b",
#     ecolor="r",
#     capsize=5,
#     label="Incertidumbre",
# )

# Personalización del gráfico
# ax.set_title("Ley de Malus", va="bottom")
ax.set_rlabel_position(95)
ax.set_rticks(np.arange(0, 0.5, 0.1))  # Less radial ticks
ax.legend()

# Mostrar la gráfica
fig.savefig("Exp5_analisis_imagen/plot_malus_a.png", dpi=300)
plt.show()
