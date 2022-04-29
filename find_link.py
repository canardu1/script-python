import requests
from bs4 import BeautifulSoup
 
 
url = "https://mypushop.com/shops/?latitude=41.4887992&longitude=12.5982912&page=14"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
