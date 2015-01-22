from django.contrib import admin
from userapp.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal information:', {'fields':['firstname', 'lastname', 'email']})
    ]
    list_display = ('firstname', 'lastname', 'email')

admin.site.register(User, UserAdmin)