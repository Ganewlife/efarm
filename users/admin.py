from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','phone_number', 'sex', 'is_farm_owner', 'is_farm_manager','is_assistant_farm_manager', 'is_team_leader', 'is_farm_worker')
    