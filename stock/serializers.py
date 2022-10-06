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