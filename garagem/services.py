import requests

BASE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles"


def decodificar_vin(vin, ano_modelo=""):
    url = f"{BASE_URL}/DecodeVinValues/{vin}?format=json"

    if ano_modelo:
        url += f"&modelyear={ano_modelo}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    resultados = data.get("Results", [])

    if resultados:
        return resultados[0]

    return {}