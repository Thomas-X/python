import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

## Set OS env to variables
emailusr = os.getenv("EMAIL_USERNAME")
emailpwd = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("EMAIL_RECIPIENT")

def checkForLaptopsIwantToBuy():
    html = requests.get("https://www.coolblue.nl/zoeken?query=xps+15+9570")
    cookie = {
        '__Secure-TnetID': '0Q7smI8XgrHVeAD0fH8486t9LFt7SU71',
        'tc': '1529056456%2C1529056456'
     }
    htmlTweakers = requests.get("https://tweakers.net/pricewatch/zoeken/?keyword=xps+15+9570#filter:q1bKTq0szy9KUbJSqigoVjA0VbA0NTdQ0lECiqUWuWWm5oCkSjJzU2FiwQWpyZ5AQV3DWgA", cookies=cookie)
    soup = BeautifulSoup(html.text, "html.parser")
    soupTweakers = BeautifulSoup(htmlTweakers.text, "html.parser")
    productTitlesTweakers = soupTweakers.find_all("a", class_="editionName")
    productTitles = soup.find_all("a", class_="product__title js-product-title")
    sendMail = False
    for productTitlesTag in productTitles:
        productTitle = productTitlesTag.string
        if (productTitle.find('9570') != -1):
            sendMail = true

    for productTitlesTweakersTag in productTitlesTweakers:
        productTitleTweakers = productTitlesTweakersTag.string
        if(productTitleTweakers.find('XPS 9570') != -1):
            sendMail = True
    
    return sendMail

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
except:
    print 'Something went wrong connecting to smtp server...'

server.login(emailusr, emailpwd)

if checkForLaptopsIwantToBuy() == True:
    emailusr = os.getenv("EMAIL_USERNAME")
    emailpwd = os.getenv("EMAIL_PASSWORD")
    msg = MIMEMultipart()
    msg['To'] = recipient
    msg['Subject'] = 'XPS 15 9570 IS OP COOLBLUE / TWEAKERS'
    msg.attach(MIMEText('BUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOWBUY NOW', 'plain'))
    server.sendmail(emailusr, recipient, msg.as_string())
exit()
