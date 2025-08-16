import requests
import pprint

api_key = "59b44a9d51d54f299ff143040252603"
link_api = "http://api.weatherapi.com/v1/current.json"

# Parâmetros da requisição: chave da API e localização desejada
params = {
    "key": api_key,
    "q": "São Paulo",
    "lang": "pt" 
}

resposta = requests.get(link_api, params=params)


if resposta.status_code == 200:
    dados = resposta.json()
    pprint.pprint(dados)

# status code
# 200 -> requisição bem-sucedida
# 300 -> redirecionada
# 400 -> erro do cliente (requisição malformada)
# 500 -> erro no servidor
