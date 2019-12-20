from django.contrib import admin
from dolanysygy.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class WelayatlarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Welayatlar,WelayatlarAdmin)

class EdaralarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Edaralar,EdaralarAdmin)

class BolumlerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bolumler,BolumlerAdmin)

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(File,FileAdmin)

class HasabatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hasabat,HasabatAdmin)

class UlanyjyAdmin(UserAdmin):
    model = Ulanyjy
    list_display = ['ady', 'username',]

admin.site.register(Ulanyjy,UlanyjyAdmin)