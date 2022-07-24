from rest_framework import serializers
from commerce.models import *


class Client_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'matcode', 'name', 'model', 'description', 'serial_number',
                  'waranty', 'provider', 'sale_price', 'purchase_price', 'quantity']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'contact', 'mail', 'company', 'location',
                  'category', 'phone', 'postcode', 'product']


class Order_ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Client
        fields = ['id', 'date', 'quantity', 'client', 'product']
