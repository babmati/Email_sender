import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

###ykgredkbasqdzzrr


html= Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Byron Arias'
email['to'] = 'wesu18@hotmail.com'
email['subject'] = 'you won 1,000,000 dollars!'


email.set_content('I am Python Master!') # this is one way or this
###email.set_content(html.substitute(name='Tintin'), 'html')   ##this is using html
#otros cam
with smtplib.SMTP(host='smtp.gmail.com' , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('bettersayb@gmail.com', '*********') #this will need personal password
    smtp.send_message(email)
    print('all good boss')
