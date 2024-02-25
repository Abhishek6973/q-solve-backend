import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json

def send_email_fun(subject, message, from_email, to_emails, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_emails, msg.as_string())

def send_email(otp, to_emails):
    subject = "Otp reset for qsolve"
    message  = f"your otp for reset your password is :{otp} "
    from_email = "abhishek86649@gmail.com"
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587
    smtp_username = "abhishek86649@gmail.com"
    smtp_password = "igqaelfyingkgruh"
    print(" credentials :", smtp_username, " ", smtp_password)
    send_email_fun(subject, message, from_email, to_emails, smtp_server, smtp_port, smtp_username, smtp_password)