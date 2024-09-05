from django.contrib import admin

from company.models import Company, Job


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'location')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'employment_type', 'vacancy')
    list_filter = ('company', )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
