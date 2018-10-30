from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = ['user','liked_products']
    list_filter = ['user']
    class Meta:
        model = Like