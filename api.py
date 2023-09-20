import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
print(response.json())