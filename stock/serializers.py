from xml.dom import ValidationErr
from rest_framework import serializers
from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name'
        )
class ProductSerializer(serializers.ModelSerializer):  
    category = serializers.StringRelatedField() #foreign key ile bağlı olanları string karşılığını almak için
    category_id = serializers.IntegerField(write_only=True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField(write_only=True) # id si görmek istiyorsa gerek yok many true vardı bir de o 1den fazla varsa döndürür

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'category_id',
            'brand',
            'brand_id',
            'stock',

        )

        read_only_fields = ('stock',)  # sadece readonly için post işleminde geçersiz

class FirmSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'phone',
            'address'
        )

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    firm = serializers.StringRelatedField() #foreign key ile bağlı olanları string karşılığını almak için
    firm_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'firm',
            'firm_id',
            'transaction',
            'product',
            'product_id',
            'price',
            'price_total'
        )

        read_only_fields = ('price_total',)  # sadece readonly için post işleminde geçersiz
        
        def validate(self, data): #gelen out işlemi eksiye düşüyorsa  yapma 
            if data.get('transaction') == 0: #data aslında burada yukarıdaki fieldsların hepsi
                product = Product.objects.get(id=data.get('product_id'))
                if data.get('quantity') > product.stock:
                    raise serializers.ValidationErr(
                        f'Dont have enough stock. Current stock is {product.stock}'
                    )
            return data
