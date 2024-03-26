import requests
from bs4 import BeautifulSoup


html_code = requests.get('https://readovka67.ru/?ysclid=lu8o7hrpp0916201053').text
soup = BeautifulSoup(html_code,'lxml')

title = soup.find('div')
print(title.text)

news = soup.find_all('div', class_='container')
for new in news:
    title_text = new.find('div', class_='scrollBar__scroller block-news-list')
    news_text2 = new.find('div', class_='block-img-link')
    print(title_text.text, news_text2.text)