import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 14})

# Read the CSV file
data = pd.read_csv(r"linealidad.csv")

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
    label=f"Ajuste lineal: \n $y={slope:.1f}x+{intercept:.1f}$",
    color="black",
)
# Plot approximation 0.5 - (x - np.pi/4)
def taylor_approx(x, I):
    return I * (0.5 - (x - np.pi/4))

# Fit the parameter I
popt, pcov = curve_fit(taylor_approx, x, y)
I_opt = popt[0]

# Plot the approximation with the fitted parameter
plt.plot(x, taylor_approx(x, I_opt), label=rf"${I_opt:.1f}(0.5 - (\theta - \frac{{\pi}}{{4}}))$", color="blue", linestyle="--")

# Add labels and title
plt.xlabel("Ángulo (rad)")
plt.ylabel("Intensidad (lux)")
plt.legend()
plt.grid(alpha=0.3)
# Set the x and y limits to only show the data
plt.xlim([min(x) - 2 * xerr, max(x) + 2 * xerr])
plt.ylim([0, 750])
plt.subplots_adjust(top=0.9)
# Save the plot with a resolution of 400 DPI
plt.savefig(r"plot_linealidad.png", dpi=400)
# Show the plot
plt.show()
