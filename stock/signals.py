from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Transaction

@receiver(pre_save, sender=Transaction)  #transactionu dinliyor, pre_save yapmadan receiver dekorator u değişiklik yapıyor
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:  #pricetotal yoksa 
        instance.price_total = instance.quantity * instance.price