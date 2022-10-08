from rest_framework import viewsets, filters
from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Transaction
)
from .serializers import(
    BrandSerializer,
    CategoryProductsSerializer,
    CategorySerializer,
    FirmSerializer,
    ProductSerializer,
    TransactionSerializer
)
from django_filters.rest_framework import DjangoFilterBackend

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['name'] # hangi field a göre search edecek 
    filterset_fields = ['name']

    def get_serializer_class(self):
        if self.request.query_params.get('name'):  # name e göre aratmak için sorgulama. url e ?name= gibi geliyor.
            # query_params ?name..&id= gibi buralardaki query_paramslar nested olarak yazabiliriz.
            return CategoryProductsSerializer        #sorgu varsa bunu yoksa alttakini
        else:
            return super().get_serializer_class()  # böylece nested arama yaptık category de

class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['name'] 

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    filterset_fields = ['category', 'brand']
    search_fields = ['name'] 

class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['name'] 

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    filterset_fields = ['firm', 'transaction', 'product']
    search_fields = ['firm'] 

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)