import os
import smtplib

import self as self

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

RECEIVER_EMAIL = 'talhasay2u@gmail.com'

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'this is test python email'
    body = 'hi, \n how are you'
    msg = f'Subject: {subject} \n\n {body}'


    smtp.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, msg)

