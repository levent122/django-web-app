from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','realtor','price','is_published','date']
    list_editable = ['is_published']
    search_fields = ['title','realtor','price','date','description','city','district','address']
    list_filter = ['date']
    list_per_page = 25
    class Meta:
        model = Product