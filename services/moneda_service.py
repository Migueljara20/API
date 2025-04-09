import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"

def convertir_moneda(from_currency: str, to_currency: str, amount: float) -> dict:
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    print("API KEY:", API_KEY)

    if response.status_code != 200:
        raise Exception(f"Error al consumir ExchangeRate API: {response.text}")

    data = response.json()
    return {
        "moneda_origen": from_currency,
        "moneda_destino": to_currency,
        "monto_original": amount,
        "monto_convertido": data.get("conversion_result"),
        "tasa_conversion": data.get("conversion_rate")
    }