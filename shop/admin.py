from django.contrib import admin

from shop.models import Wine, Occasion, Mood, Goods

admin.site.register(Goods)
admin.site.register(Wine)
admin.site.register(Occasion)
admin.site.register(Mood)

