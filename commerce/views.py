from commerce.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from commerce.serializers import *

class Client_CategoryViewset(ModelViewSet):

    serializer_class = Client_CategorySerializer

    def get_queryset(self):
        return Client_Category.objects.all()


class Order_ClientViewset(ModelViewSet):

    serializer_class = Order_ClientSerializer

    def get_queryset(self):
        return Order_Client.objects.all()


class ClientViewset(ModelViewSet):

    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ProductViewset(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
