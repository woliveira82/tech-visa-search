from django.contrib import admin
from .models import Company

class CompanyList(admin.ModelAdmin):
    list_display = ('tax_number', 'name', 'certification_date', 'expiration_date')
    list_display_links = ('tax_number', 'name')
    search_fields = ('tax_number', 'name')
    list_per_page = 20

admin.site.register(Company, CompanyList)
