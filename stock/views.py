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