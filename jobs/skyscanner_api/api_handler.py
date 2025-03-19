import requests


class SkyScannerHandler():
    """Classe handler
    """
    @staticmethod
    def requests(url: str, api_key: str, host: str, params= None):
        """Handler de requisição para api do skyscanner

        Args:
            url (str): Endpoint a ser acessado
            api_key (str): Chave de conexão
            host (str): Host da conexão
            params (_type_, optional): Parametros da requisição. Defaults to None.
        """

        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": host
        }

        response = requests.get(url, headers=headers, params=params)
        return(response.json())
