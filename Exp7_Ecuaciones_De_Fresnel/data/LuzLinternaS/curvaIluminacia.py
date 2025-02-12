
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definir los directorios donde están los archivos de datos
directorios = ["data/LuzLaserS/organizados_por_grados/","data/LuzLinternaS/organizados_por_grados/", "data/LuzLinternaP/organizados_por_grados/", "data/LuzLinternaSinPolarizar/organizados_por_grados/"]

# Almacenar los resultados
todos_los_resultados = []

# Procesar cada directorio
for directorio in directorios:
    for file_name in os.listdir(directorio):
        file_path = os.path.join(directorio, file_name)
        
        # Verificar que el archivo sea un CSV
        if file_name.endswith(".csv"):
            df = pd.read_csv(file_path)
            
            # Tomar la segunda columna (iluminancia)
            if df.shape[1] > 1:
                data = df.iloc[:, 1].dropna().values  # Segunda columna con iluminancia
            
                # Calcular la media y la incertidumbre
                mean_illuminance = np.mean(data)
                uncertainty = np.std(data, ddof=1) / np.sqrt(len(data))
            
                # Extraer ángulo desde el nombre del archivo
                angle = ''.join(filter(str.isdigit, file_name))
            
                # Guardar resultados con el nombre del directorio
                todos_los_resultados.append([directorio, float(angle), mean_illuminance, uncertainty])

# Crear un DataFrame con los resultados
results_df = pd.DataFrame(todos_los_resultados, columns=["Directorio", "Ángulo (grados)", "Iluminancia promedio (lx)", "Incertidumbre (lx)"])

# Convertir ángulos a radianes
results_df["Ángulo (radianes)"] = np.radians(results_df["Ángulo (grados)"])

print(results_df)



# Graficar iluminancia vs ángulo en radianes con barras de error para cada directorio
plt.figure(figsize=(8, 5))
for directorio in results_df["Directorio"].unique():
    subset = results_df[results_df["Directorio"] == directorio]
    plt.errorbar(subset["Ángulo (radianes)"], 
                 subset["Iluminancia promedio (lx)"], 
                 yerr=subset["Incertidumbre (lx)"], 
                 fmt='o', capsize=5, label=f"{directorio}")

# Configuración de la gráfica
plt.xlabel("Ángulo (radianes)")
plt.ylabel("Iluminancia (lx)")
plt.title("Iluminancia vs Ángulo con Incertidumbre (Múltiples Directorios)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Mostrar la gráfica
plt.show()
