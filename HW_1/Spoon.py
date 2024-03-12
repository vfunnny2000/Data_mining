from passwords import SPOON 
import requests
import json

url = "https://api.spoonacular.com/recipes/complexSearch"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept":  "*/*"
}

params = {
    "apiKey": SPOON,
    "query": "beef",
}

response = requests.get(url, params=params, headers=headers)

if response.ok:
    data = json.loads(response.text)
    count = 1
    for item in data["results"]:
        print(item["title"])
        print(item["image"])
else:
    print("Error")