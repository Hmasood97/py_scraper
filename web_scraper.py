import requests
import re
from bs4 import BeautifulSoup
import smtplib
#Amazon link for Nintendo Switch Pro Controller
URL = 'https://www.amazon.com/Nintendo-Switch-Pro-Controller/dp/B01NAWKYZ0/ref=sr_1_3?keywords=nintendo%2Bpro%2Bcontroller&qid=1577552832&sr=8-3&th=1'

headers = {"User=Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'}


page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
#soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup1.find(id="productTitle").get_text()

price = soup1.find(id="priceblock_ourprice").get_text()

price2 = re.sub(r"[\n\t\s]*", "", price)
finalPrice = float(price2[1:3])


#price up to two digits
print(finalPrice)


if(finalPrice <56):
    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('pythonmasood97@gmail.com''YOURPASSWORD')

    subject = "SWITCH PRO CONTROLLER PRICE DOWN"

    body = "check link https://www.amazon.com/Nintendo-Switch-Pro-Controller/dp/B01NAWKYZ0/ref=sr_1_3?keywords=switch%2Bpro%2Bcontroller&qid=1577724144&sr=8-3&th=1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pythonmasood97@gmail.com', 
        'hisham9977@gmail.com',
        msg)

    print("sent email")

    server.quit()
