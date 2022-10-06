from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Transaction, Product
#burada database ile ilgili işlemleri yapıyoruz o yüzden uyarı mesajı serializers tan döndürebiliriz.
@receiver(pre_save, sender=Transaction)  #transactionu dinliyor, pre_save yapmadan receiver dekorator u değişiklik yapıyor
def calculate_total_price(sender, instance, **kwargs):
    if not instance.price_total:  #pricetotal yoksa 
        instance.price_total = instance.quantity * instance.price


@receiver(post_save, sender=Transaction)
def update_stock(sender, instance, **kwargs):
    product = Product.objects.get(id=instance.product_id)
    if instance.transaction == 1:
        if not product.stock:  #ilk null olarak geldiği için böyle yaptık
            product.stock = instance.quantity
        else:
            product.stock += instance.quantity
    else:
        product.stock -= instance.quantity

    product.save()