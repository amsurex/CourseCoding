from bs4 import BeautifulSoup as bs
import requests

city = input('Введите город на англиской литерации: ') #пример - moskva
url = f'https://pogoda.mail.ru/prognoz/{city}/'

response = requests.get(url)
soup = bs(response.text,"lxml")

data = soup.find('div', class_='information__content__temperature')
weather = data.find ('span').text 

print(f'Погода в городе {city} сейчас %s градусов.' %weather)