from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email='nav219.996gupta@gmail.com'
    from_password='nav261999'
    to_email=email

    subject='Height Data'
    message='Hey there your height is <strong>%s</strong>.Average height of all is <strong>%s</strong> which is calculated among <strong>%s</strong> entries'% (height,average_height,count)

    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['to']=to_email
    msg['from']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)