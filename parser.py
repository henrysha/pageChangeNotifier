import requests, filecmp, smtplib
from difflib import HtmlDiff
from bs4 import BeautifulSoup
from email.mime.text import MIMEText

senderId = 'YOUR GMAIL ID'
senderPw = 'YOUR GMAIL PASSWORD'
emailAddr = 'ADDRESS TO SEND MAIL'
url = 'URL TO PARSE'

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

new_file = 'content.html'
original_file = 'original.html'
file = open(new_file, 'w')
for table in soup.find_all('table'):
    data = table.encode('utf-8') + '\n'
    file.write(data)
file.close
if not(filecmp.cmp(new_file,original_file,shallow=False)):
    print 'not identical'
    with open(original_file, 'w') as orig:
        with open(new_file, 'r') as new:
            data = new.read()
            orig.write(data)
    send_email(senderId,senderPw,emailAddr,'New MATH286 Homework Alert!','New homework has been uploaded!\n go to : '+url+' to check it out!')

