from django.contrib import admin
from soporte.models import Soporte


# class SoporteAdmin(admin.ModelAdmin):
#     readonly_fiels =('user',)
    
#     def save_model(self, request, obj, form, change):
        
#        if not obj.user_id:
#             obj.user_id = request.user.id
        
#        obj.save()



admin.site.register(Soporte)