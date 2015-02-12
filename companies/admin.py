from django.contrib import admin
from companies.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question']
	list_display = ('company_name', 'stage', 'city', 'mattermark_score', 'total_funding', 'momentum_score', 'employees', 'investors', 'cached_growth_score')
	list_filter = ['stage']
	search_fields = ['company_name', 'investors']

admin.site.register(Company, CompanyAdmin)

