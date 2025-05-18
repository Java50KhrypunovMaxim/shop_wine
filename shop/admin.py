from django.contrib import admin

from shop.models import Wine, Mood, Goods, Glass, Corkscrew, Country, Producer

admin.site.register(Goods)
admin.site.register(Wine)
admin.site.register(Mood)
admin.site.register(Glass)
admin.site.register(Corkscrew)
admin.site.register(Country)
admin.site.register(Producer)
