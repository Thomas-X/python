from src.json_utils import load_json_file, create_json_file
import os
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mailer:

    def __init__(self):
        self.path = os.path.join(os.path.expanduser('~/gitrepos/python/slack-automail/recipients.json'))
        # self.recipients = load_json_file(self.path) 
        self.recipients = ['thomaszwarts@gmail.com']

    def mail(self):
        fromaddr = "noreplybot1337@gmail.com"
        toaddr = "thomaszwarts@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Onofficiële Slack van AD Software Development"

        body = "YOUR MESSAGE HERE"
        msg.attach(MIMEText(body, 'plain'))

        # send mail logic       
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "YOUR PASSWORD")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
