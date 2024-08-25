from django.contrib import admin

from company.models import Company, Job


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_active', 'location')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'employment_type', 'vacancy', 'is_active')
    list_filter = ('company', 'is_active')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
