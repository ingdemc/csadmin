from django.contrib import admin
from cargasemantica.models import Metadatos


# Register your models here.
class MetadatosAdmin(admin.ModelAdmin):
    readonly_fiels =('user','fechacreacion')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Metadatos, MetadatosAdmin)