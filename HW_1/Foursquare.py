import requests
from passwords import CLIENT_ID, CLIENT_SECRET
import json



CLIENT_ID = CLIENT_ID 
CLIENT_SECRET = CLIENT_SECRET 
VERSION = '20240311' # Foursquare API version




# Введите свой ключ API Foursquare
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# Запросите у пользователя категорию
category = input("Введите интересующую вас категорию (например, кофейни, музеи, парки): ")

# Задайте параметры запроса
params = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'v': '20240311',
    'query': category,
    'near': 'Москва',
    'limit': 5
}

# Отправьте запрос к API Foursquare
response = requests.get('https://api.foursquare.com/v2/venues/search', params=params)

# Извлеките данные из ответа
venues = response.json()['response']['venues']

# Выведите название, адрес и рейтинг каждого заведения
for venue in venues:
    print(f"Название: {venue['name']}")
    print(f"Адрес: {venue['location']['formattedAddress']}")
    print(f"Рейтинг: {venue['rating']}")
    print()
    
    
    
# ************************** ВАРИАНТ ДРУГОЙ ****************

import requests
import json

# Получаем категорию от пользователя
category = input("Введите интересующую вас категорию: ")

# Создаем запрос к API Foursquare
url = "https://api.foursquare.com/v2/venues/explore"
params = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "v": "20240311",
    "near": "Москва",
    "category": category,
    "limit": 10
}

# Отправляем запрос и получаем ответ
response = requests.get(url, params=params)

# Проверяем статус ответа
if response.status_code != 200:
    print("Ошибка при получении данных от API Foursquare")
    exit()

# Получаем данные из ответа
data = response.json()

# Получаем список заведений
venues = data["response"]["groups"][0]["items"]

# Выводим информацию о каждом заведении
for venue in venues:
    print(f"Название: {venue['name']}")
    print(f"Адрес: {venue['location']['formattedAddress']}")
    print(f"Рейтинг: {venue['rating']}")
    print("-" * 10)