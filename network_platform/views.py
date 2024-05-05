from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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
from users.permissions import IsActive


class ContactCreateAPIView(generics.CreateAPIView):
    """
    Создание контактной информации.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной контактной информации.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ContactListAPIView(generics.ListAPIView):
    """
    Просмотр всех контактных информаций.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ContactUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение контактной информации
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление контактной информации
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Создание продукта.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение продукта.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductListAPIView(generics.ListAPIView):
    """
    Просмотр всех продуктов.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ElectroFactoryCreateAPIView(generics.CreateAPIView):
    """
    Создание завода.
    """
    serializer_class = ElectroFactorySerializer
    queryset = ElectronicsFactory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ElectroFactoryListAPIView(generics.ListAPIView):
    """
    Просмотр всех заводов.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer
    permission_classes = [IsAuthenticated, IsActive]


class ElectroFactoryRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного завода.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer
    permission_classes = [IsAuthenticated, IsActive]


class ElectroFactoryUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение завода.
    """
    serializer_class = ElectroFactorySerializer
    queryset = ElectronicsFactory.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ElectroFactoryDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление завода.
    """
    queryset = ElectronicsFactory.objects.all()
    serializer_class = ElectroFactorySerializer
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkCreateAPIView(generics.CreateAPIView):
    """
    Создание розничной сети.
    """
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной розничной сети.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkListAPIView(generics.ListAPIView):
    """
    Просмотр всех розничных сетей.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение розничной сети.
    """
    serializer_class = RetailNetworkSerializer
    queryset = RetailNetwork.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class RetailNetworkDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление розничной сети.
    """
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class SoleTraderCreateAPIView(generics.CreateAPIView):
    """
    Создание индивидуального предпринимателя.
    """
    serializer_class = SoleTraderSerializer
    queryset = SoleTrader.objects.all()
    permission_classes = [IsAuthenticated]


class SoleTraderListAPIView(generics.ListAPIView):
    """
    Просмотр всех индивидуальных предпринимателей.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer
    permission_classes = [IsAuthenticated, IsActive]


class SoleTraderRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одного индивидуального предпринимателя.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer
    permission_classes = [IsAuthenticated, IsActive]


class SoleTraderUpdateAPIView(generics.UpdateAPIView):
    """
    Изменение индивидуального предпринимателя.
    """
    serializer_class = SoleTraderSerializer
    queryset = SoleTrader.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class SoleTraderDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление индивидуального предпринимателя.
    """
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer
    permission_classes = [IsAuthenticated, IsActive]
