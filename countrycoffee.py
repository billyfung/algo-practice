import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_coffee_production'
r = requests.get(url)
soup = BeautifulSoup(r.content)
countries = []
table = soup.find('table', {'class':'wikitable'})
datalist = table.find_all('a')
for x in datalist:
    countries.append(x.string)
