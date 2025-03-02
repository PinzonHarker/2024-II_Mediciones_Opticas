import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as wid
#from scipy.optimize import curve_fit
#from scipy.ndimage import gaussian_filter1d
import colorcet as cc
import os
import copy
#from matplotlib.patches import FancyBboxPatch
import uncertainties as un
#from uncertainties.umath import *
import simpy as sp
mpl.rcParams.update(
    {
        "legend.fontsize": 20,
        "axes.labelsize": 24,  # Updated from 20 to 24
        "axes.titlesize": 24,
        "xtick.labelsize": 20,
        "ytick.labelsize": 20,
        "figure.titlesize": 24,
        "axes.titlepad": 10,
        "text.usetex": True,
        "font.family": "Times New Roman",
        "mathtext.fontset": "dejavusans",
        "font.size": 20,
        "axes.labelweight": "bold",
        "axes.grid.which": "both",
        "axes.grid": True,
        "grid.alpha": 0.5,
        "axes.formatter.limits": (-3, 3),  # Use scientific notation for values outside the range 10^-3 to 10^3
        'figure.subplot.bottom': 0.2,
        'figure.subplot.left': 0.2,  # Added more space on the left side
    }
)

colors = cc.glasbey_category10
# Configuracion de colores
k = 0

# Rotar la lista: número positivo para rotar a la derecha, negativo para rotar a la izquierda
colors = colors[-k:] + colors[:-k]

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=colors)


# Read the CSV file
data = pd.read_csv(r"C:\Users\pinzo\OneDrive - Universidad Nacional de Colombia\Docs\Universidad\2024-2\Mediciones en Óptica\2024-II_Mediciones_Opticas\Exp5b_Malus_camara\linealidad.csv")
plt.figure(figsize=(8, 5))
# Assuming the CSV has columns 'x', 'y', and 'yerr' for x values, y values, and y errors respectively
x = np.radians(range(20, 75, 5))
y = data["Mean"]
xerr = np.radians(2.5)
yerr = data["ERR"]

# Create the plot
plt.errorbar(
    x, y, xerr=xerr, yerr=yerr, fmt="o", ecolor="#b20000", mfc="red", mec="blue", capsize=5, label="Mediciones"
)

# Perform linear regression
slope, intercept = np.polyfit(x, y, 1)
regression_line = slope * x + intercept

# Plot the regression line
plt.axline(
    (0, intercept),
    slope=slope,
    label=f"Ajuste lineal",
    color="black",
    lw=3
)
# Plot approximation 0.5 - (x - np.pi/4)
def taylor_approx(x, I):
    return I * (0.5 - (x - np.pi/4))

# Fit the parameter I
popt, pcov = curve_fit(taylor_approx, x, y)
I_opt = popt[0]

# Plot the approximation with the fitted parameter
# Extend the range of x for extrapolation
x_extended = np.linspace(x.min() - 0.1, x.max() + 0.1, 100)
plt.plot(x_extended, taylor_approx(x_extended, I_opt), label=rf"${I_opt:.1f}(0.5 - (\theta - \frac{{\pi}}{{4}}))$", color="blue", linestyle="--", lw=3)

# Add labels and title
plt.xlabel("Ángulo (rad)")
plt.ylabel("Iluminancia (lx)")
plt.legend()
# Set the x and y limits to only show the data
plt.xlim([0.29, 1.337])
plt.ylim([67, 817])
# Save the plot with a resolution of 400 DPI
plt.savefig(r"C:\Users\pinzo\OneDrive - Universidad Nacional de Colombia\Docs\Universidad\2024-2\Mediciones en Óptica\2024-II_Mediciones_Opticas\Exp5b_Ley_De_Malus\plot_linealidad.pdf")

