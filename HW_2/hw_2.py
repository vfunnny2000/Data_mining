# может и не самый быстрый, но рабочий вариант
import time
import requests
from bs4 import BeautifulSoup
import json

start_time = time.time()
url = 'http://books.toscrape.com/catalogue/'
all_books = []

def get_book_info(book):
    book_info = {}
    book_info['name'] = book.select_one('h3 a').text
    book_info['price'] = float(book.select_one('p.price_color').text[1:])
    availability = book.select_one('p.availability').text.strip()
    book_info['availability'] = availability
    if availability == 'In stock':
        book_url = url + book.select_one('h3 a')['href']
        book_page = requests.get(book_url)
        book_soup = BeautifulSoup(book_page.content, 'html.parser')
        available_text = book_soup.select_one('p.availability').text
        # book_info['available'] = int(available_text.split()[2])
        book_info['available'] = int(available_text.split()[2].strip('()'))
        description = book_soup.find('meta', {'name': 'description'})['content']
        book_info['description'] = description
    else:
        book_info['available'] = 0
        book_info['description'] = None
    return book_info

count = 1
while True:
    page_url = url + f'page-{count}.html'
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    if len(books) == 0:
        break
    for book in books:
        book_info = get_book_info(book)
        all_books.append(book_info)
    print("\033c")
    print(f"Обрабатываем страницу № {count}, прошло {time.time() - start_time:.2f} секунд")
    count += 1

filename = 'books.json'
with open(filename, 'w') as file:
    json.dump(all_books, file)

end_time = time.time()
print(f"Обработано за {end_time - start_time:.2f} секунд {len(all_books)} книг, сохранено в {filename}")
