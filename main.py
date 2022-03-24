import os
import smtplib
from datetime import date
import time
from datetime import datetime, timedelta, timezone
from keep_running import keep_running


sent = 0
pings = 0
seconds = 0
my_secret = os.environ['pass']
passw = str(my_secret)
words = os.environ['words']
maillist = os.environ['maillist']
words = words.split('\n')
# if input("Testing? Y/N: ") == 'y':
#   maillist = os.environ['test']
#   print("test mode enabled")
# else:
#   pass
print(f"email/s being used are: {maillist}")
def email():
  global sent
  today = date.today()
  today = str(today)
  t = today.split('-')
  
  f_date = date(2021, 6, 19)
  l_date = date(int(t[0]),int(t[1]),int(t[2]))
  delta = l_date - f_date
  index = (delta.days)
  index +=3
  
  wordle = words[index]
  wordle = wordle.split()
  
  # print(f'The wordle today is: {wordle[5]}')
  
  wordle = str(wordle[5])
  
  date_and_time = str(datetime.now())

  message = """From: From WordleBot <wordlemessenger@gmail.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: The Wordle Today

<h1 style = "color: black; padding: 1px;">The Wordle Today:</h1>
<p style = "color: white; padding: 1px; height: 1px; font-size:0.5px;">(This email contains wordle spoilers. Answer is hidden in the preview.)#############################################################################################################################################</p>
<div style="color:green;font-weight: bold;font-size: 30px;">"""+ wordle +"""</div>
<p></p>
<div style="font-style: italic;color: black;">That's the wordle.</div>
<div><p></p></div>
<div><p></p></div>
<p></p>
<div><small>Bot Made by Deez nuts</small></div>
<div><small style = "color: red;">If you would like to opt out of this service, please message me on Discord.</small><div>
<div style = "font-size: 10px;">[""" + date_and_time +  """ UTC]</div>"""
  
  # print(message)
  
  for email in maillist.split('\n'):
    try:
      server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
      server.login("wordlemessenger@gmail.com",passw)
      server.sendmail("wordlemessenger@gmail.com",email,message)
      print(f"Email sucessfully sent to: {email}")
      sent += 1
    except:
      print(f"Email unsucessfully sent to: {email}")

  
  
  server.quit()
  print("SMTP session terminated")


print("Welcome to the wordle email service:")
keep_running()

deploy = "00:00"

while True:
  currenttime = (datetime.now(timezone(timedelta(hours=-4), 'EST')))
  currenttime = str(currenttime)
  currenttime = currenttime.split()[1].split('.')[0].split(':')
  currenttime = currenttime[0] + ':' + currenttime[1]
  print(f"Time: {currenttime}, pings: {pings}, emails: {sent}, seconds: {seconds}. Deploy: {deploy}")
  seconds+=10
  if currenttime == deploy:
    print("Sending Email")
    email()
    seconds+=60
    time.sleep(60)
    
  else:
    pass
  
  time.sleep(10)
  pings+= 1
