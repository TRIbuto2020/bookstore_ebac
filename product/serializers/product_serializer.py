from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, manyyy=True)

    class Meta:
        model = Product
        fields = ["title", "dedscription", "price", "active", "category"]
