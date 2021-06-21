import bs4
from requests.sessions import session
from config import username, password
import requests
from bs4 import BeautifulSoup

url = 'https://prenotami.esteri.it'
loginurl = 'https://prenotami.esteri.it/UserArea'
headersNice = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
                'origin': url, 'referer': url+'/'}

payload = {
    'Email': username,
    'Password': password
}

s = requests.session()

loginreq = s.post(loginurl, headers = headersNice, data = payload)
print(loginreq.status_code)

cookies = loginreq.cookies

soup = BeautifulSoup(s.get(loginurl).text, 'html.parser')
figurine = soup.find('main', id = 'main')
print(figurine)