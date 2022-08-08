from django.contrib import admin
from .models import Category, Product

class IdAdmin(admin.ModelAdmin):
    prepopulated_fields={"title":("title",)}

admin.site.register(Product, IdAdmin)
admin.site.register(Category, IdAdmin)

