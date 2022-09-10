from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta: 
    model: Product = Product
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "description",
      "price",
      "get_image",
      "get_thumbnail",
    )

class CategorySerializer(serializers.ModelSerializer):
  products = ProductSerializer(many=True)
  class Meta:
    model: Category = Category
    fields = (
      "name",
      "id",
      "products",
      "get_absolute_url",

    )