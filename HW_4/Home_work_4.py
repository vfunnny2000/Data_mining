# Цель этого кода - извлечь данные из таблицы курсов валют с веб-сайта Центрального банка России 
# (https://cbr.ru/currency_base/daily), парсинг HTML-содержимого страницы, извлечение данных из таблицы 
# с использованием XPath и сохранение данных в CSV-файл.

# 1. Импортируются необходимые библиотеки: requests для отправки HTTP запросов, lxml для парсинга HTML и csv для работы с CSV файлами.

# 2. Устанавливается URL адрес сайта, куда отправляется GET-запрос, а также добавляются заголовки для имитирования пользователя 
# с помощью строки агента пользователя.

# 3. Отправляется GET-запрос на указанный сайт. Если ответный код равен 200 (успешный запрос), продолжается выполнение кода.

# 4. HTML-содержимое страницы парсится с помощью библиотеки lxml.

# 5. С помощью XPath выбираются элементы таблицы с курсами валют.

# 6. Для каждой строки таблицы извлекаются данные: цифровой код валюты, название валюты и ее курс.

# 7. Полученные данные добавляются в список `data` в формате [code, currency, rate].

# 8. Данные записываются в CSV-файл `currency_data.csv`. Первая строка CSV-файла содержит заголовки столбцов: 'Цифр. код', 'Валюта', 'Курс'.

# 9. В случае успешного извлечения и сохранения данных, выводится сообщение об успешном завершении операции. В случае ошибки 
# при получении данных, выводится соответствующее сообщение.


import requests
from lxml import html
import csv

# Отправка HTTP GET-запроса на веб-сайт
url = 'https://cbr.ru/currency_base/daily'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
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