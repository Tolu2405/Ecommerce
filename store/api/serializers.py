from asyncore import read
from rest_framework import serializers
from store.models import Products,Category
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(source='category.name')
    uploaded_by=serializers.CharField(source='uploaded_by.username')
    class Meta:
        model = Products
        fields = '__all__'
        
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Category
        fields = "__all__"
        