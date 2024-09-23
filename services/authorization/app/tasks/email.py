import json
import smtplib
import time
import hashlib

from celery import shared_task

from app.config import settings
from app.utils.email import email_constructor

server = smtplib.SMTP(settings.EMAIL_SERVER, 587)
server.ehlo()
server.starttls()
server.login(settings.EMAIL_LOGIN, settings.EMAIL_PASSWORD)


@shared_task
async def verify_email(email: str):
    payload = {
        "email": email,
        "expiry": time.time() + settings.EMAIL_EXPIRE,
    }
    code = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
    link = settings.email_verify_url + code
    server.sendmail(settings.EMAIL_LOGIN, email, email_constructor(link).as_string())
