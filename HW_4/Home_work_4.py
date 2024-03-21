import requests
from lxml import html
import csv

# Отправка HTTP GET-запроса на веб-сайт
url = 'https://cbr.ru/currency_base/daily'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Парсинг HTML-содержимого
    tree = html.fromstring(response.content)
    
    # Выражение XPath для выбора элементов таблицы
    rows = tree.xpath('//table[@class="data"]/tbody/tr')
    
    # Извлечение данных из таблицы
    data = []
    for row in rows:
        code = row.xpath('./td[1]/text()')
        currency = row.xpath('./td[4]/text()')
        rate = row.xpath('./td[5]/text()')
        data.append([code, currency, rate])
    
    # Сохранение данных в CSV-файл
    with open('currency_data.csv', 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(['Цифр. код', 'Валюта', 'Курс'])
        writer.writerows(data)
        
    print("Данные успешно извлечены и сохранены в CSV-файл 'currency_data.csv'.")
else:
    print("Ошибка при получении данных. Проверьте URL и подключение к интернету.")