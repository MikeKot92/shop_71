from django.contrib import admin
from unfold.admin import ModelAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username']


@admin.register(EmailVerification)
class EmailVerificationAdmin(ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ['code', 'user', 'expiration', 'created']
    readonly_fields = ['created']
