from django.contrib import admin

from .models import motor, presion, msg,action,temp,vanne

admin.site.register(action)
admin.site.register(presion)
admin.site.register(msg)
admin.site.register(temp)
admin.site.register(motor)
admin.site.register(vanne)
