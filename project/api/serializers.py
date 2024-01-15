from rest_framework import serializers

from .models import Product, Manufacturer, Category


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProductSerializers(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['title', 'size', 'manufacturer', 'category', 'price']

    def create(self, validated_data):
        manufacturer_data = validated_data.pop('manufacturer')
        category_data = validated_data.pop('category')

        manufacturer_instance, _ = Manufacturer.objects.get_or_create(**manufacturer_data)
        category_instance, _ = Category.objects.get_or_create(**category_data)

        product = Product.objects.create(manufacturer=manufacturer_instance, category=category_instance, **validated_data)
        return product

    def update(self, instance, validated_data):
        manufacturer_data = validated_data.pop('manufacturer')
        category_data = validated_data.pop('category')

        instance.title = validated_data.get('title', instance.title)
        instance.size = validated_data.get('size', instance.size)
        instance.price = validated_data.get('price', instance.price)

        manufacturer_instance, _ = Manufacturer.objects.get_or_create(**manufacturer_data)
        category_instance, _ = Category.objects.get_or_create(**category_data)

        instance.manufacturer = manufacturer_instance
        instance.category = category_instance

        instance.save()
        return instance