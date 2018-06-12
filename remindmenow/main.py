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
    soup = BeautifulSoup(html.text, "html.parser")
    productTitles = soup.find_all("a", class_="product__title js-product-title")
    sendMail = False
    for productTitlesTag in productTitles:
        productTitle = productTitlesTag.string
        if (productTitle.find('9570') != -1):
            sendMail = true

    return sendMail

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
except:
    print 'Something went wrong connecting to smtp server...'

server.login(emailusr, emailpwd)
msg = MIMEMultipart()
msg['To'] = recipient
msg['Subject'] = 'HGi from python'
msg.attach(MIMEText('hello there', 'plain'))

server.sendmail(emailusr, recipient, msg.as_string())

if checkForLaptopsIwantToBuy():
    emailusr = os.getenv("EMAIL_USERNAME")
    emailpwd = os.getenv("EMAIL_PASSWORD")

exit()
