from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response

from network_platform.models import (
    Contact,
    Product,
    ElectronicsFactory,
    RetailNetwork,
    SoleTrader
)

from network_platform.serializers import (
    ContactSerializer,
    ProductSerializer,
    ElectroFactorySerializer,
    RetailNetworkSerializer,
    SoleTraderSerializer
)


class ContactCreateAPIView(generics.CreateAPIView):
    """
    Создание контактной информации.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной контактной информации.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListAPIView(generics.ListAPIView):
    """
    Просмотр всех контактных информаций.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение контактной информации
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление контактной информации
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Создание продукта.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение продукта.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListAPIView(generics.ListAPIView):
    """
    Просмотр всех продуктов.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ElectroFactoryCreateAPIView(generics.CreateAPIView):
    """
    Создание завода.
    """
    serializer_class = ElectroFactorySerializer
    queryset = ElectronicsFactory.objects.all()


class ElectroFactoryListAPIView(generics.ListAPIView):
    """
    Просмотр всех заводов.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer


class ElectroFactoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного завода.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer


class ElectroFactoryUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение завода.
    """
    serializer_class = ElectroFactorySerializer
    queryset = ElectronicsFactory.objects.all()


class ElectroFactoryDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление завода.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer


class RetailNetworkCreateAPIView(generics.CreateAPIView):
    """
    Создание розничной сети.
    """
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()


class RetailNetworkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной розничной сети.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkListAPIView(generics.ListAPIView):
    """
    Просмотр всех розничных сетей.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение розничной сети.
    """
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()


class RetailNetworkDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление розничной сети.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class SoleTraderCreateAPIView(generics.CreateAPIView):
    """
    Создание индивидуального предпринимателя.
    """
    serializer_class = SoleTraderSerializer
    queryset = SoleTrader.objects.all()


class SoleTraderListAPIView(generics.ListAPIView):
    """
    Просмотр всех индивидуальных предпринимателей.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer


class SoleTraderRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного индивидуального предпринимателя.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer


class SoleTraderUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение индивидуального предпринимателя.
    """
    serializer_class = SoleTraderSerializer
    queryset = SoleTrader.objects.all()


class SoleTraderDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление индивидуального предпринимателя.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer
