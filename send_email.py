import smtplib, ssl, os
from email.message import EmailMessage


# get email and password from environment variables
SMTP_SERVER = os.environ.get('SMTP_SERVER')
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')
PORT = 465  # For SSL

# set up email content
msg = EmailMessage()
msg.set_content("Hello Underworld!")
msg['Subject'] = "Hello Underworld from Python Scripts!"
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_RECIPIENT

# send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg, from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_RECIPIENT)