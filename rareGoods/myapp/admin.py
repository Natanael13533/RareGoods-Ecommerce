from django.contrib import admin
from myapp.models import Product, Category, Blog, Comment, Reply, Lokasi

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Lokasi)