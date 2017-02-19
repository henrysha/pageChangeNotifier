# pageChangeNotifier
Sends Email whenever specific webpage changes
----
# Dependencies
`requests` and `BeautifulSoup4` must be installed.
```
pip install requests
sudo pip install bs4
```
Run this command if you don't have them.
---

# USAGE
change the `senderId`, `senderPw`, `emailAddr`, `url`, `emailSubject` and `emailContent` in `parse.py` to your need
```
senderId = 'YOUR GMAIL ID'
senderPw = 'YOUR GMAIL PASSWORD'
emailAddr = 'ADDRESS TO SEND MAIL'
url = 'URL TO PARSE'
emailSubject = 'EMAIL SUBJECT'
emailContent = 'EMAIL CONTENT'
```
whenever you run the script, you will get an email notifying the the page change

I have added the .cron file that runs the script every 6 hours.

After you clone the repo, do the custom edits (infos) and do
```
crontab parse.cron
```
To automatically parse and compare the webpage
### Note
>Parser parses table from the page, so it only checks the difference in the tables of the page.
>This is due to the original intended usage of the author, so feel free to modify when you use.

When you upload this to AWS and try to run it there, gmail SMTP servers won't work.

Use AWS SES and modify `send_email` function to your needs
```
FROM = 'Email@Address.tosendfrom'
```
and
```
server = smtplib.SMTP("your.path.to.ses.smtp.server", 587)
```
to send the email from the SES

### Contact
If you have any ideas, or comments, feel free to [email](mailto:sha16@illinois.edu) me

If you feel like you want to hire me, please visit my [Linkedin](https://www.linkedin.com/in/henryseongwookha) or [email](mailto:sha16@illinois.edu) me!
