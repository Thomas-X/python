from src.json_utils import load_json_file, create_json_file
import os
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    def __init__(self):
        self.path = os.path.join(os.path.expanduser('~/gitrepos/python/slack-automail/recipients.json'))
        # self.recipients = load_json_file(self.path) 
    
        # tmp test recipient email
        self.recipients = ['']
        self.credentials = load_json_file(os.path.join(os.getcwd(), 'credentials.json'))
        self.senderemail = self.credentials.get('email')
        self.pwd = self.credentials.get('password')

    def send_mail(self, idx):
        fromaddr = self.senderemail
        toaddr = self.recipients[idx]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Onofficiële Slack uitnodiging voor AD Software Development"
        body = """Hi,

Dit is een uitnodiging voor de onofficiele Slack voor AD Software Development. Voel je niet verplicht, het is iets puur wat (mij, Thomas Zwarts) een goed idee leek. 
De Slack is bedoelt om opleidings-specifieke info te delen met de hele opleiding, maar ook voor die ene vette dank meme die je moet delen met anderen en algemeen gechat tussen elkaar, sinds je ook tussen personen een gezamelijke chat kan maken. 
In principe kan iedereen met een @student-windesheim.nl email de Slack gewoon joinen, maar hou het alsjeblieft gewoon bij AD Software Development studenten :). Tevens zijn de rechten vrij laks, je kan channels aanmaken e.d, misbruik het niet. 

Link om te joinen: https://adsoftwaredevelopment.slack.com/signup

Met vriendelijke groet,

Thomas Zwarts"""
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        self.server.sendmail(fromaddr, toaddr, text)

    def mail(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.senderemail, self.pwd)

        for idx, val in enumerate(self.recipients):
            self.send_mail(idx)

        self.server.quit()
