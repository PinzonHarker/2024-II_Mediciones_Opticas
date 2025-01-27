"""Graficación de los valores de irradiancia de las imagenes de prueba (práctica 5a)
solo para las restantes de imageJ"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Leer el archivo Excel
csv_red = pd.read_excel(r"Exp5b_Malus_camara\malus_mean_area1.xlsx", sheet_name="red")
csv_green = pd.read_excel(r"Exp5b_Malus_camara\malus_mean_area1.xlsx", sheet_name="green")
csv_blue = pd.read_excel(r"Exp5b_Malus_camara\malus_mean_area2.xlsx", sheet_name="blue")

# Extraer columnas como arrays de NumPy
# errors = [df["Rstd"].to_numpy()]

# Angulos
angles = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65])
remaining = np.arange(70, 360 + 1, 10)
angles = np.concatenate((angles, remaining)) * np.pi / 180

# Crear la figura y los ejes polares
fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

# Formato de las gráficas
format_plot = dict(marker="o", ls="-", lw="0.5", fillstyle="none")
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# Gráfica de los puntos con barras de error radiales
# ----RED
ax.errorbar(
    angles,
    csv_red["Mean"].to_numpy(),
    yerr=csv_red["ERR"].to_numpy(),
    fmt="none",
    color=colors["red"],
    alpha=0.5,
)
ax.plot(
    angles,
    csv_red["Mean"].to_numpy(),
    label="Intensidad Roja",
    color=colors["red"],
    alpha=0.5,
    **format_plot
)
# ---- BLUE
ax.errorbar(
    angles,
    csv_blue["Mean"].to_numpy(),
    yerr=csv_blue["ERR"].to_numpy(),
    fmt="none",
    color=colors["blue"],
    alpha=0.5,
)

ax.plot(
    angles,
    csv_blue["Mean"].to_numpy(),
    label="Intensidad Azul",
    color=colors["blue"],
    alpha=0.5,
    **format_plot
)

# ---- GREEN
ax.errorbar(
    angles,
    csv_green["Mean"].to_numpy(),
    yerr=csv_green["ERR"].to_numpy(),
    fmt="none",
    color=colors["green"],
    alpha=0.5,
)

ax.plot(
    angles,
    csv_green["Mean"].to_numpy(),
    label="Intensidad Verde",
    color=colors["green"],
    alpha=0.5,  # Reduce alpha for transparency
    **format_plot
)

# graficar curva teórica I = I0 * cos(theta)^2
# Define the theoretical Malus' Law function
def malus_law(theta, I0):
    return I0 * np.cos(theta) ** 2

# Fit the I0 parameter to the red intensity data
popt, _ = curve_fit(malus_law, angles, csv_blue["Mean"].to_numpy())
I0_fitted = popt[0]

# Generate the theoretical curve with the fitted I0
angles_fine = np.linspace(0, 2 * np.pi, 1000)
I_fitted = malus_law(angles_fine, I0_fitted)

# Plot the fitted theoretical curve
ax.plot(angles_fine, I_fitted, label=f"I = {I0_fitted:.2f} * cos(θ)^2", color="black", lw=1)

# Personalización del gráfico
# ax.set_title("Ley de Malus", va="bottom")
ax.set_rlabel_position(95)
#ax.set_rticks(np.arange(0, 1, 0.1))  # Less radial ticks
ax.legend()

# Mostrar la gráfica
fig.savefig("Exp5b_Malus_camara/5b_plot_camera_mean_tiny.png", dpi=400)
plt.show()
