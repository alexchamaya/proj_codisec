import requests

class APIServiceDNIVehicular:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def consultar_dni_vehicular(self):
        url = self.base_url
        try:
            response = requests.get(url)
            response.raise_for_status()  # Verificar si la respuesta fue exitosa
            return response.json()  # Retornar los datos en formato JSON
        except requests.exceptions.RequestException as e:
            print(f"Error al consultar la API: {e}")
            return None