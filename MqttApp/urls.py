from .views import *
from django.urls import path

urlpatterns = [

    path('presion/last',PresionDefineLast.as_view() ),
    path('action/last',ActionDefineLast.as_view() ),
    path('msg/last',MsgDefineLast.as_view() ),
    path('temp/last',TempDefineLast.as_view() ),
    path('motor/last',MotorDefineLast.as_view() ),

]