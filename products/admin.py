from django.contrib import admin
from .models import product, category

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(product, productAdmin)
admin.site.register(category, categoryAdmin)
