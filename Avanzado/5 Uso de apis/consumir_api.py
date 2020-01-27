import requests

r = requests.get("https://pokeapi.co/api/v2/pokemon/treecko/")
#requests.put()
#requests.delete()

print(r.json())