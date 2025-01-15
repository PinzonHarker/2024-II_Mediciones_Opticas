"""Graficación de los valores de irradiancia de las imagenes de prueba (práctica 5a)
solo para las restantes de imageJ para el pixel único"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Leer el archivo Excel
csv_red = pd.read_csv("Exp5_analisis_imagen/data_pixel_red.csv")
csv_green = pd.read_csv("Exp5_analisis_imagen/data_pixel_green.csv")
csv_blue = pd.read_csv("Exp5_analisis_imagen/data_pixel_blue.csv")

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
# ----RED
ax.errorbar(
    angles,
    csv_red["Mean"].to_numpy(),
    yerr=csv_red["StdDev"].to_numpy(),
    fmt="none",
    color=colors["red"],
)
ax.plot(
    angles,
    csv_red["Mean"].to_numpy(),
    label="Irradiancia Roja",
    color=colors["red"],
    **format_plot
)
# ---- BLUE
ax.errorbar(
    angles,
    csv_blue["Mean"].to_numpy(),
    yerr=csv_blue["StdDev"].to_numpy(),
    fmt="none",
    color=colors["blue"],
)

ax.plot(
    angles,
    csv_green["Mean"].to_numpy(),
    label="Irradiancia Verde",
    color=colors["green"],
    **format_plot
)

# ---- GREEN
ax.errorbar(
    angles,
    csv_green["Mean"].to_numpy(),
    yerr=csv_green["StdDev"].to_numpy(),
    fmt="none",
    color=colors["green"],
)

ax.plot(
    angles,
    csv_blue["Mean"].to_numpy(),
    label="Irradiancia Azul",
    color=colors["blue"],
    **format_plot
)

# Personalización del gráfico
# ax.set_title("Ley de Malus", va="bottom")
ax.set_rlabel_position(95)
#ax.set_rticks(np.arange(0, 1, 0.1))  # Less radial ticks
ax.legend()

# Mostrar la gráfica
fig.savefig("Exp5_analisis_imagen/5a_plot_imagej_pixel.png", dpi=300)
plt.show()
