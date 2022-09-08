import smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import username_email,pass_email    

receiver = 'erra_anregi@yahoo.co.id'
#message
msg = MIMEMultipart("alternative")
msg['Subject']='Company Dealing'
msg['From']='Reya'
msg['to']='erra_anregi@yahoo.co.id'

#template
html = open("meeting #3/Final-Project/template.html")
template = MIMEText(html.read(),"html")
msg.attach(template)


#send mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    
    server.login(username_email,pass_email)
    server.sendmail(
        from_addr=username_email,to_addrs=receiver,msg=msg.as_string()
    )
    server.quit()

    print("Email Terkirim")