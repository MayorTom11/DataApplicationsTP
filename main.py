import requests
import config
import pandas as pd

def consulta():
    # Consulta a la API
    response = requests.get(f"https://v6.exchangerate-api.com/v6/{config.forex_API}/latest/USD").json()
    
    # Extraer las tasas de cambio del JSON
    rates = response['conversion_rates']
    
    # Convertir las tasas a un df
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Exchange Rate'])
    
    return df

def quota():
    quota = requests.get(f"https://v6.exchangerate-api.com/v6/{config.forex_API}/quota").json()
    print(quota)


df_tasas = consulta()
print(df_tasas)