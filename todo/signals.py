from django.db.models.signals import ModelSignal
from django.dispatch import receiver

user_registered=ModelSignal()

@receiver(user_registered)
def send_email(sender,user,**kwargs):
    print("Email is sent to",user)
    