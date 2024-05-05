from rest_framework import serializers
from django.core.exceptions import ValidationError

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

    def validate(self, attrs):
        """
        Метод проверяет, что заполнено
        одно поле: завод или розничная сеть.
        """
        provider_factory = attrs.get('provider_factory')
        provider_retailer = attrs.get('provider_retailer')

        if provider_factory and provider_retailer:
            raise serializers.ValidationError(
                "Одновременно не может быть два поставщика")
        if not provider_factory and not provider_retailer:
            raise serializers.ValidationError(
                "Хотя бы один поставщик должен быть указан")

        return attrs
