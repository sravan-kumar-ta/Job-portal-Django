from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'username',
                    'role',
                ),
            },
        ),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

    list_display = ('username', 'id', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    filter_horizontal = ()
    ordering = ("-id",)


admin.site.register(get_user_model(), CustomUserAdmin)
