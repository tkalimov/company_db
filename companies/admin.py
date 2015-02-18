from django.contrib import admin
from companies.models import Company
from django.utils.translation import ugettext_lazy as _
import pdb
# Register your models here.

class EmployeeCountListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Number of employees'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'employee_count'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('10', 'Fewer than 10'),
            ('20', '10-20'),
            ('50', '20-50'),
            ('100', '50-100'),
            ('200', '100-200'),
            ('500', '200-500'),
			('1000', '500-1000'),
			('10000', 'Greater than 1000'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        # pdb.set_trace()

        if self.value() == '10':
            return queryset.filter(employees__gte=0, employees__lte=10)

        if self.value() == '20':
            return queryset.filter(employees__gte=10, employees__lte=20)

        if self.value() == '50':
            return queryset.filter(employees__gte=20, employees__lte=50)

        if self.value() == '100':
            return queryset.filter(employees__gte=50, employees__lte=100)

        if self.value() == '200':
            return queryset.filter(employees__gte=100, employees__lte=200)

        if self.value() == '500':
            return queryset.filter(employees__gte=200, employees__lte=500)

        if self.value() == '1000':
            return queryset.filter(employees__gte=500, employees__lte=1000)

        if self.value() == '10000':
            return queryset.filter(employees__gte=1000)

class CompanyAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question']
	list_display = ('company_name', 'stage', 'city', 'mattermark_score', 'total_funding', 'momentum_score', 'employees', 'investors', 'cached_growth_score')
	list_filter = ['stage', EmployeeCountListFilter]
	search_fields = ['company_name', 'investors']

admin.site.register(Company, CompanyAdmin)

