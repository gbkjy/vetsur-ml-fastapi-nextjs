import pandas as pd

# Nota: Este script sirve para obtener rápidamente las medianas del dataset original.
# Estos valores se usan en la API para rellenar datos faltantes (imputación).
try:
    df = pd.read_csv('api/caso1_vetsur.csv', encoding='latin1')
except:
    df = pd.read_csv('caso1_vetsur.csv', encoding='latin1')

# Nota: Calculamos la mediana del monto y los costos para asegurar que el modelo no reciba valores nulos.
print(f"MEDIANA_MONTO:{df['monto_cobrado'].median()}")
print(f"MEDIANA_MEDS:{df['costo_medicamento'].median()}")
