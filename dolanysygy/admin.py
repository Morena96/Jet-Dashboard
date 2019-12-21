from django.contrib import admin
from dolanysygy.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class WelayatlarAdmin(admin.ModelAdmin):
    pass

admin.site.register(Welayatlar,WelayatlarAdmin)

class EdaralarAdmin(admin.ModelAdmin):
    list_display = ['ady','welaýaty']
    list_filter= ('welaýaty',)
    list_per_page=30
admin.site.register(Edaralar,EdaralarAdmin)

class BolumlerAdmin(admin.ModelAdmin):
    list_display = ['ady']

admin.site.register(Bolumler,BolumlerAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ['ady','eýesi','welaýaty','edarasy','bölümi','görnüşi','dokument']
    date_hierarchy = 'döredilen_senesi'
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "eýesi":
            kwargs["initial"] = request.user.id
            kwargs['disabled'] = True
        if db_field.name == "welaýaty":
            kwargs["initial"] = request.user.welaýaty.id
            kwargs['disabled'] = True
        if db_field.name == "edarasy":
            kwargs["initial"] = request.user.edarasy.id
            kwargs['disabled'] = True
        if db_field.name == "bölümi":
            kwargs["initial"] = request.user.bölümi.id
            kwargs['disabled'] = True
        if db_field.name == "görnüşi":
            kwargs["queryset"] = Hasabat.objects.filter(bölümi=request.user.bölümi)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
#    empty_value_display = '-empty-'
admin.site.register(File,FileAdmin)

class HasabatAdmin(admin.ModelAdmin):
    list_display = ['ady','bölümi']

admin.site.register(Hasabat,HasabatAdmin)

class UlanyjyAdmin(UserAdmin):
    list_display = ['username','ady','welaýaty','edarasy','bölümi','mac_adresi']
    fieldsets = (
    (None, {
        'fields': ( 'username','ady','welaýaty','edarasy','bölümi','password','mac_adresi')
    }),
    ('Goşmaça Maglumatlar', {
        'classes': ('collapse',),
        'fields': ('first_name', 'last_name','groups','is_staff'),
    }),
    )

admin.site.register(Ulanyjy,UlanyjyAdmin)