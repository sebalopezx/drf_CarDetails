# import pandas as pd
# import json
# import os

# archivo_csv_marcas  = os.path.join(os.path.dirname(__file__), 'marcas.csv')
# archivo_csv_modelos  = os.path.join(os.path.dirname(__file__), 'modelos.csv')
# archivo_csv_anios  = os.path.join(os.path.dirname(__file__), 'anios.csv')

# # Cargar archivos CSV
# marcas_df  = pd.read_csv(archivo_csv_marcas)
# modelos_df  = pd.read_csv(archivo_csv_modelos)
# anios_df  = pd.read_csv(archivo_csv_anios)


# # Combinar DataFrames
# # Primero, combinar marcas y modelos
# merged_df = pd.merge(marcas_df, modelos_df, left_on='idmake', right_on='fkmake', how='inner')

# # Luego, combinar con anios
# merged_df = pd.merge(merged_df, anios_df, left_on='idmodel', right_on='fkmodel', how='inner')

# # Agregar un nuevo ID
# merged_df['id'] = range(1, len(merged_df) + 1)

# # Seleccionar las columnas necesarias
# columns_to_keep = ['id','make', 'slugmake', 'model', 'slugmodel', 'year']
# result_df = merged_df[columns_to_keep]

# # Convertir a JSON y guardar
# json_result = result_df.to_dict(orient='records')

# with open('data.json', 'w') as json_file:
#     json.dump(json_result, json_file, indent=2)


# FORMA 2

# import pandas as pd
# import json
# import os

# archivo_csv_marcas = os.path.join(os.path.dirname(__file__), 'marcas.csv')
# archivo_csv_modelos = os.path.join(os.path.dirname(__file__), 'modelos.csv')
# archivo_csv_anios = os.path.join(os.path.dirname(__file__), 'anios.csv')

# # Cargar archivos CSV
# marcas_df = pd.read_csv(archivo_csv_marcas)
# modelos_df = pd.read_csv(archivo_csv_modelos)
# anios_df = pd.read_csv(archivo_csv_anios)

# # Combinar DataFrames
# # Primero, combinar marcas y modelos
# merged_df = pd.merge(marcas_df, modelos_df, left_on='idmake', right_on='fkmake', how='inner')

# # Luego, combinar con anios
# merged_df = pd.merge(merged_df, anios_df, left_on='idmodel', right_on='fkmodel', how='inner')

# # Agregar un nuevo ID
# merged_df['id'] = range(1, len(merged_df) + 1)

# # Seleccionar las columnas necesarias
# columns_to_keep = ['id', 'make', 'slugmake', 'model', 'slugmodel', 'year']

# # Convertir a un formato jerárquico con años incrustados en modelos
# result_df = merged_df.groupby(['id', 'make', 'slugmake', 'model', 'slugmodel']).apply(
#     lambda x: x[['year']].to_dict(orient='records')).reset_index(name='years')

# # Convertir a JSON y guardar
# json_result = result_df.to_dict(orient='records')

# with open('data2.json', 'w') as json_file:
#     json.dump(json_result, json_file, indent=2)
 


# FORMA 3



# import pandas as pd
# import json
# import os

# archivo_csv_marcas = os.path.join(os.path.dirname(__file__), 'marcas.csv')
# archivo_csv_modelos = os.path.join(os.path.dirname(__file__), 'modelos.csv')
# archivo_csv_anios = os.path.join(os.path.dirname(__file__), 'anios.csv')

# # Cargar archivos CSV
# marcas_df = pd.read_csv(archivo_csv_marcas)
# modelos_df = pd.read_csv(archivo_csv_modelos)
# anios_df = pd.read_csv(archivo_csv_anios)

# # Combinar DataFrames
# # Primero, combinar marcas y modelos
# merged_df = pd.merge(marcas_df, modelos_df, left_on='idmake', right_on='fkmake', how='inner')

# # Luego, combinar con anios
# merged_df = pd.merge(merged_df, anios_df, left_on='idmodel', right_on='fkmodel', how='inner')

# # Seleccionar las columnas necesarias
# columns_to_keep = ['idmake', 'slugmake', 'make', 'idmodel', 'slugmodel', 'model', 'idyear', 'year']

# # Convertir a JSON y guardar
# json_result = []
# for index, row in merged_df.iterrows():
#     entry = {
#         "id": f"{row['idmake']}_{row['idmodel']}_{row['idyear']}",  # Combinación única de idmake, idmodel, e idyear
#         "make": row['make'],
#         "slugmake": row['slugmake'],
#         "model": row['model'],
#         "slugmodel": row['slugmodel'],
#         "year": row['year']
#     }
#     json_result.append(entry)

# with open('data.json', 'w') as json_file:
#     json.dump(json_result, json_file, indent=2)


# forma 4

import pandas as pd
import json
import os

# Rutas a los archivos CSV
archivo_csv_marcas = os.path.join(os.path.dirname(__file__), 'marcas.csv')
archivo_csv_modelos = os.path.join(os.path.dirname(__file__), 'modelos.csv')
archivo_csv_anios = os.path.join(os.path.dirname(__file__), 'anios.csv')

# Cargar archivos CSV
marcas_df = pd.read_csv(archivo_csv_marcas)
modelos_df = pd.read_csv(archivo_csv_modelos)
anios_df = pd.read_csv(archivo_csv_anios)

# Combinar DataFrames
# Primero, combinar marcas y modelos
merged_df = pd.merge(marcas_df, modelos_df, left_on='idmake', right_on='fkmake', how='inner')

# Luego se combina con años
merged_df = pd.merge(merged_df, anios_df, left_on='idmodel', right_on='fkmodel', how='inner')

# Agrupar por modelo y construir la lista de años
result_df = merged_df.groupby(['idmake', 'make', 'slugmake', 'idmodel', 'model',  'slugmodel'])['year'].apply(lambda x: x.unique().tolist()).reset_index()

# Convertir a JSON y guardar
json_result = result_df.to_dict(orient='records')

with open('data.json', 'w') as json_file:
    json.dump(json_result, json_file, indent=2)