from rest_framework.serializers import ModelSerializer

from product.models import Products


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
