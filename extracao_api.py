import requests
from typing import List, Dict, Optional
from config import API_BASE_URL, API_KEY

class CoinCapAPI:
    def __init__(self):
        """Essa função tem como objetivo inicializar o cliente com a URL base e os cabeçalhos de autenticação."""
        self._base_url = API_BASE_URL
        self._headers = {
            'Authorization': f'Bearer {API_KEY}'
        }

    def get_assets(self, limit: int = 2000) -> Optional[List[Dict]]:
        """
        Essa função tem como objetivo buscar a lista completa de criptomoedas (ativos) da API. A API da CoinCap pagina os resultados, então fazemos um loop para garantir que pegamos todos os ativos.
        """
        all_assets = []
        offset = 0
        
        while True:
            endpoint = f"{self._base_url}/assets"
            params = {
                'limit': limit,
                'offset': offset
            }
            
            try:
                print(f"Buscando {limit} ativos com offset {offset}")
                response = requests.get(endpoint, headers=self._headers, params=params)

                response.raise_for_status()
                
                data = response.json().get('data', [])
                
                if not data:
                    break
                
                all_assets.extend(data)
                offset += limit

            except requests.exceptions.RequestException as e:
                print(f"Erro ao se comunicar com a API da CoinCap: {e}")
                return None
        
        print(f"Total de {len(all_assets)} ativos encontrados.")

        return all_assets
