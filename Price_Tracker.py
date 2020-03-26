import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Sapiens-Humankind-Yuval-Noah-Harari-ebook/dp/B00K7ED54M/ref=pd_rhf_gw_s_zg_ebk_0_5/258-6432220-2407902?_encoding=UTF8&pd_rd_i=B00K7ED54M&pd_rd_r=6fe42aba-837a-4eea-b977-2b326f0723e8&pd_rd_w=zhMqT&pd_rd_wg=IWO89&pf_rd_p=732b64d9-c412-47ee-b756-86b3b7974b9e&pf_rd_r=4H8QQXRF7S3N3SPA2MJY&psc=1&refRID=4H8QQXRF7S3N3SPA2MJY'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    page= requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "ebooksProductTitle").get_text()

    #price = soup.findAll("span", class_= "a-size-medium a-color-price")

    for price in soup.findAll(attrs={'class' : 'a-size-medium a-color-price'}):
        price = price.text.strip()

    converted_price =  float(price[0:5])

    if(converted_price < 179):
        send_email()

    print(title.strip())
    print(converted_price)

def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('crosstalk789@gmail.com', '#password')

    subject = 'Price'

    body = 'Check link https://www.amazon.in/Sapiens-Humankind-Yuval-Noah-Harari-ebook/dp/B00K7ED54M/ref=pd_rhf_gw_s_zg_ebk_0_5/258-6432220-2407902?_encoding=UTF8&pd_rd_i=B00K7ED54M&pd_rd_r=6fe42aba-837a-4eea-b977-2b326f0723e8&pd_rd_w=zhMqT&pd_rd_wg=IWO89&pf_rd_p=732b64d9-c412-47ee-b756-86b3b7974b9e&pf_rd_r=4H8QQXRF7S3N3SPA2MJY&psc=1&refRID=4H8QQXRF7S3N3SPA2MJY'

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail('crosstalk789@gmail.com', 'pritamdash1997@gmail.com', msg)

    print('Email sent !')

    server.quit()

check_price()

