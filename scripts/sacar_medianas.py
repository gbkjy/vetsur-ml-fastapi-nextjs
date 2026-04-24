import pandas as pd
try:
    df = pd.read_csv('api/caso1_vetsur.csv', encoding='latin1')
except:
    df = pd.read_csv('caso1_vetsur.csv', encoding='latin1')

print(f"MEDIANA_MONTO:{df['monto_cobrado'].median()}")
print(f"MEDIANA_MEDS:{df['costo_medicamento'].median()}")
