import requests

api_key = "59b44a9d51d54f299ff143040252603"
link_api = "http://api.weatherapi.com/v1/current.json"

# Parâmetros da requisição: chave da API e localização desejada
params = {
    "key": api_key,
    "q": "São Paulo"  # você pode trocar por qualquer cidade
}

resposta = requests.get(link_api, params=params)

print(resposta.status_code)
print(resposta.content)

# status code
# 200 -> requisição bem-sucedida
# 300 -> redirecionada
# 400 -> erro do cliente (requisição malformada)
# 500 -> erro no servidor
