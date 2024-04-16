from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def task_manage(a,b):
    time.sleep(2)   
    print(a+b)
    return a+b

@shared_task
def Test_task(id):
    print("Hey celery beat is runing")
    print(id)



@shared_task
def Email():
    res=send_mail(
    "Subject here",
    "Here is the message.",
    "sender_email",
    ["recepient email"],
    fail_silently=False,
    )
    print(res)




