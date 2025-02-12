# Reimportar las librerías tras el reinicio del entorno
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos extraídos de la imagen
angulos_grados = np.array([30, 50, 60, 65, 70])
iluminancia = np.array([6163.4353, 24197.12963, 39188.91228, 57368.42565, 73187.77217])/73187.77217
incertidumbre = np.array([0.068281, 0.863878,
                          1.501598, 1.892725, 0.636748])/73187.77217

# Convertir ángulos a radianes
angulos_radianes = np.radians(angulos_grados)

# Definir el modelo teórico de Fresnel para r_perp^2 con n_i = 1
def fresnel_r_perp_squared(theta_i, n_t):
    theta_t = np.arcsin((1 / n_t) * np.sin(theta_i))  # Ley de Snell
    r_perp_squared = ((np.cos(theta_i) - n_t * np.cos(theta_t)) / 
                      (np.cos(theta_i) + n_t * np.cos(theta_t))) ** 2
    return r_perp_squared

# Ajustar la curva a los datos experimentales
popt, _ = curve_fit(fresnel_r_perp_squared, angulos_radianes, iluminancia, p0=[1.4])

# Graficar los datos experimentales con barras de error
plt.figure(figsize=(8, 5))
plt.errorbar(angulos_radianes, iluminancia, yerr=incertidumbre, fmt='o', label="Datos experimentales", capsize=5)

# Graficar la curva ajustada
theta_fit = np.linspace(min(angulos_radianes), max(angulos_radianes), 100)
iluminancia_fit = fresnel_r_perp_squared(theta_fit, *popt)
plt.plot(theta_fit, iluminancia_fit, label=f"Ajuste con n_t = {popt[0]:.3f}", linestyle='--', color='r')

# Configuración de la gráfica
plt.xlabel("Ángulo (radianes)")
plt.ylabel("Iluminancia (lx)")
plt.title("Ajuste de Iluminancia con modelo de Fresnel")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# Mostrar la gráfica
plt.show()
