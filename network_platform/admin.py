from django.contrib import admin

from network_platform.models import (
    Contact,
    Product,
    ElectronicsFactory,
    RetailNetwork,
    SoleTrader
)

admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(ElectronicsFactory)
admin.site.register(RetailNetwork)
admin.site.register(SoleTrader)
