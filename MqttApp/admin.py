from django.contrib import admin

from .models import motor, presion, msg,action

admin.site.register(action)
admin.site.register(presion)
admin.site.register(msg)

admin.site.register(motor)
