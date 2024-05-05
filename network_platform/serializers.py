from rest_framework import serializers

from network_platform.models import (
    Contact,
    Product,
    ElectronicsFactory)


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактной информации.
    """

    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продукта.
    """

    class Meta:
        model = Product
        fields = '__all__'


class ElectroFactorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для завода.
    """

    class Meta:
        model = ElectronicsFactory
        fields = '__all__'


class RetailNetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для розничной сети.
    """

    class Meta:
        model = ElectronicsFactory
        fields = '__all__'


class SoleTraderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для индивидуального предпринимателя.
    """

    class Meta:
        model = ElectronicsFactory
        fields = '__all__'
