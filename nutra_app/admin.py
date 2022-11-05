from django.contrib import admin

from nutra_app.models import AdminUser, ApiUsersUser, CustomUser, DeveloperUser

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(DeveloperUser)
admin.site.register(ApiUsersUser)











