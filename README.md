# pageChangeNotifier
Sends Email whenever specific webpage changes
----
#USAGE
change the senderId, senderPw, emailAddr, url, emailSubject and emailContent in 'parse.py' to your need
whenever you run the script, you will get an email notifying the the page change
I have added the .cron file that runs the script every 6 hours.
After you clone the repo, do the custom edits (infos) and do
| crontab parse.cron
To automatically parse and compare the webpage
### Note
Parser parses table from the page, so it only checks the difference in the tables of the page.
This is due to the original intended usage of the author, so feel free to modify when you use.
