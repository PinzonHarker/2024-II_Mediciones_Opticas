import pandas as pd
import os



def convert_xls_to_csv(input_file, output_folder=None, name=None):
    """
    Convierte un archivo .xls a uno o varios archivos .csv (uno por hoja).

    :param input_file: Ruta del archivo .xls de entrada.
    :param output_folder: Carpeta donde se guardarán los archivos CSV. Si es None, usa la misma carpeta del archivo original.
    """
    if not output_folder:
        output_folder = os.path.dirname(input_file)
    
    # Leer todas las hojas del archivo .xls
    xls = pd.read_excel(input_file, sheet_name=None, engine="xlrd")
    
    # Iterar sobre cada hoja y guardarla como CSV
    for sheet_name, df in xls.items():
        output_file = os.path.join(output_folder, f"{sheet_name}")
        df.to_csv(output_file + name+".csv", index=False, encoding="utf-8-sig")
        print(f"Archivo guardado: {output_file}")

# Ejemplo de uso
for i in range(3, 8):
    for j in [0,5]:
        convert_xls_to_csv(f"data/{i}{j}grados.xls", f"data",f"{i}{j}grados")