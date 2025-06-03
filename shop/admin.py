from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from shop.models import (
    Wine, Mood, Product, Glass,
    Corkscrew, Country, Producer,
    Order
)

class ProductAdmin(ImportExportModelAdmin):
    pass

class WineAdmin(ImportExportModelAdmin):
    pass

class MoodAdmin(ImportExportModelAdmin):
    pass

class GlassAdmin(ImportExportModelAdmin):
    pass

class CorkscrewAdmin(ImportExportModelAdmin):
    pass

class CountryAdmin(ImportExportModelAdmin):
    pass

class ProducerAdmin(ImportExportModelAdmin):
    pass

class OrderAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Mood, MoodAdmin)
admin.site.register(Glass, GlassAdmin)
admin.site.register(Corkscrew, CorkscrewAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Order, OrderAdmin)



