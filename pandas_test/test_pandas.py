import pandas as pd

# Creamos unos datos de prueba
datos = {
    'Nombre': ['Agente A', 'Agente B', 'Agente C'],
    'Nivel': [10, 20, 30]
}

df = pd.DataFrame(datos)
print("--- DataFrame creado con éxito ---")
print(df)
print("\nPromedio de Nivel:", df['Nivel'].mean())
