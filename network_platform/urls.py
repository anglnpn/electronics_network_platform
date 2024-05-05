from django.urls import path

from network_platform.apps import NetworkPlatformConfig
from network_platform.views import (
    ContactCreateAPIView, ContactListAPIView,
    ContactUpdateAPIView, ContactDeleteAPIView,
    ProductCreateAPIView, ProductListAPIView,
    ProductUpdateAPIView, ProductDeleteAPIView,
    ProductRetrieveAPIView, ElectroFactoryCreateAPIView,
    ElectroFactoryUpdateAPIView, ElectroFactoryRetrieveAPIView,
    ElectroFactoryListAPIView, ElectroFactoryDeleteAPIView,
    RetailNetworkCreateAPIView, RetailNetworkListAPIView,
    RetailNetworkUpdateAPIView, RetailNetworkDeleteAPIView,
    RetailNetworkRetrieveAPIView, SoleTraderCreateAPIView,
    SoleTraderUpdateAPIView, SoleTraderRetrieveAPIView,
    SoleTraderDeleteAPIView, SoleTraderListAPIView
)

app_name = NetworkPlatformConfig.name

urlpatterns = [
    path('contact/create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('contact/list/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact/update/<int:pk>/', ContactUpdateAPIView.as_view(), name='contact_update'),
    path('contact/delete/<int:pk>/', ContactDeleteAPIView.as_view(), name='contact_delete'),

    path('products/create/', ProductCreateAPIView.as_view(), name='products_create'),
    path('products/list/', ProductListAPIView.as_view(), name='products_list'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='products_update'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='products_delete'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='products_get'),

    path('factory/create/', ElectroFactoryCreateAPIView.as_view(), name='factory_create'),
    path('factory/list/', ElectroFactoryListAPIView.as_view(), name='factory_list'),
    path('factory/update/<int:pk>/', ElectroFactoryUpdateAPIView.as_view(), name='factory_update'),
    path('factory/delete/<int:pk>/', ElectroFactoryDeleteAPIView.as_view(), name='factory_delete'),
    path('factory/<int:pk>/', ElectroFactoryRetrieveAPIView.as_view(), name='factory_get'),

    path('retail/create/', RetailNetworkCreateAPIView.as_view(), name='retail_create'),
    path('retail/list/', RetailNetworkListAPIView.as_view(), name='retail_list'),
    path('retail/update/<int:pk>/', RetailNetworkUpdateAPIView.as_view(), name='retail_update'),
    path('retail/delete/<int:pk>/', RetailNetworkDeleteAPIView.as_view(), name='retail_delete'),
    path('retail/<int:pk>/', RetailNetworkRetrieveAPIView.as_view(), name='retail_get'),

    path('trader/create/', SoleTraderCreateAPIView.as_view(), name='entrepreneur_create'),
    path('trader/list/', SoleTraderListAPIView.as_view(), name='entrepreneur_list'),
    path('trader/update/<int:pk>/', SoleTraderUpdateAPIView.as_view(), name='entrepreneur_update'),
    path('trader/delete/<int:pk>/', SoleTraderDeleteAPIView.as_view(), name='entrepreneur_delete'),
    path('trader/<int:pk>/', SoleTraderRetrieveAPIView.as_view(), name='entrepreneur_get'),
]
