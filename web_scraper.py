import requests
from bs4 import BeautifulSoup
#Amazon link for Nintendo Switch Pro Controller
URL = 'https://www.amazon.com/Nintendo-Switch-Pro-Controller/dp/B01NAWKYZ0/ref=sr_1_3?keywords=nintendo%2Bpro%2Bcontroller&qid=1577552832&sr=8-3&th=1'

headers = {"User=Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'}


page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
#soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup1.find(id="productTitle").get_text()

price = soup1.find(id="priceblock_ourprice").get_text()

intPrice = price[0:5]

print(intPrice)
print(title.strip())

