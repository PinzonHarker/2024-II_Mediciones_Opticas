import os
import rawpy
import imageio


# Directorio donde se encuentran las imágenes .dng
# input_folder = r'C:\Users\pinzo\Downloads\Optica\malus_png\test'
# output_folder = r'C:\Users\pinzo\Downloads\Optica\malus_png\test_png'

input_folder = r'C:\Users\pinzo\OneDrive - Universidad Nacional de Colombia\Docs\Universidad\2024-2\Mediciones en Óptica\data_dif\left'
output_folder = r'data'

# Crear el directorio de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Convertir cada archivo .dng en la carpeta
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith('.dng'):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.png")
        
        # Leer el archivo .dng
        with rawpy.imread(input_path) as raw:
            # Procesar la imagen a RGB según los ajustes de la cámara
            rgb_image = raw.postprocess(use_camera_wb=True, no_auto_bright=True)
        
        # Guardar como PNG
        imageio.imsave(output_path, rgb_image)
        print(f"Convertido: {file_name} -> {output_path}")

print("¡Conversión completada!")

