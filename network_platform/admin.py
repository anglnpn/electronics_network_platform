from django.contrib import admin

from django.urls import reverse
from django.utils.html import format_html

from network_platform.models import (
    Contact,
    Product,
    ElectronicsFactory,
    RetailNetwork,
    SoleTrader
)


def clear_debt_action(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0.00
        obj.save()


clear_debt_action.short_description = "Очистить задолженность"


class ContactCityFilter(admin.SimpleListFilter):
    title = 'City'

    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = set(
            Contact.objects.values_list('city', flat=True))
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(
                contacts__city=self.value())


@admin.register(ElectronicsFactory)
class MovieAdmin(admin.ModelAdmin):
    list_filter = (ContactCityFilter,)
    list_display = (
        'name', 'contact',
        'created_date',
        'get_product_link'
    )

    def get_product_link(self, obj):
        product = obj.product
        if product:
            link = reverse(
                "admin:network_platform_product_change",
                args=[product.pk])
            return format_html(
                '<a href="{}">{}</a>',
                link, product)
        return "-"

    get_product_link.short_description = "Продукт"


@admin.register(RetailNetwork)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact',
        'get_provider_from_factory_link',
        'debt', 'created_date',
        'get_product_link'
    )

    list_display_links = (
        'get_provider_from_factory_link', 'name'
    )

    list_filter = (ContactCityFilter,)

    def get_provider_from_factory_link(self, obj):
        factory = obj.provider_factory

        if factory:
            link = reverse(
                "admin:network_platform_electronicsfactory_change",
                args=[factory.pk])
            return format_html(
                '<a href="{}">{}</a>', link, factory)

    def get_product_link(self, obj):
        product = obj.product
        if product:
            link = reverse(
                "admin:network_platform_product_change",
                args=[product.pk])
            return format_html(
                '<a href="{}">{}</a>',
                link, product)
        return "-"

    get_product_link.short_description = "Продукт"

    get_provider_from_factory_link.short_description = "Поставщик"

    actions = [clear_debt_action]


@admin.register(SoleTrader)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact',
        'get_provider_link',
        'debt', 'created_date',
        'get_product_link'
    )

    list_display_links = ('get_provider_link', 'name')

    list_filter = (ContactCityFilter,)

    def get_provider_link(self, obj):
        if obj.provider_factory:
            factory = obj.provider_factory
            link = reverse(
                "admin:network_platform_electronicsfactory_change",
                args=[factory.pk])
            return format_html(
                '<a href="{}">{}</a>', link, factory)

        elif obj.obj.provider_retailer:
            retailer = obj.provider_retailer
            link = reverse(
                "admin:network_platform_retailnetwork_change",
                args=[retailer.pk])
            return format_html(
                '<a href="{}">{}</a>', link, retailer)

    def get_product_link(self, obj):
        product = obj.product
        if product:
            link = reverse(
                "admin:network_platform_product_change",
                args=[product.pk])
            return format_html(
                '<a href="{}">{}</a>', link, product)
        return "-"

    get_product_link.short_description = "Продукт"

    get_provider_link.short_description = "Поставщик"

    actions = [clear_debt_action]


admin.site.register(Contact)

admin.site.register(Product)
