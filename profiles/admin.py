from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_street_address1')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user',)
    ordering = ('user',)

# Registra o modelo UserProfile no admin
admin.site.register(UserProfile, UserProfileAdmin)