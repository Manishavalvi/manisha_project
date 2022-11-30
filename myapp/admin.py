from django.contrib import admin

from myapp.models import *

# Register your models here.
# admin.site.register(AppoUser)
# admin.site.register(Doctor)
# admin.site.register(Contact)

@admin.register(AppoUser)
class UserAdmin(admin.ModelAdmin):
    list_display=['f_name','l_name','email','mobile','date','time']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['d_name','speciality','pic','description']

@admin.register(Contact)
class UserAdmin(admin.ModelAdmin):
    list_display=['full_name','email','subject','message']

