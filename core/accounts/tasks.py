from celery import shared_task
from core.celery import Celery
from time import sleep


@shared_task
def sendEmail():
    sleep(6)
    print('done sending email')