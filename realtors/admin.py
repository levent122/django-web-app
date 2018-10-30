from django.contrib import admin
from .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    search_fields = ['name','phone','email']
    list_filter = ['date']
    list_display = ['name','email','phone','is_mvp']
    list_editable = ['is_mvp']
    class Meta:
        model = Realtor