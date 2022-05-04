
from MqttApp.models import *
from MqttApp.serializers import *

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView,ListAPIView)

###############################################################################

class PresionDefineLast(ListCreateAPIView):
        queryset =presion.objects.all()
        serializer_class =PresionSerializer
        pagination_class = None
        presion.objects

class ActionDefineLast(ListCreateAPIView):
        queryset =action.objects.all()
        serializer_class =ActionSerializer
        pagination_class = None
        action.objects

class MsgDefineLast(ListCreateAPIView):
        queryset =msg.objects.all()
        serializer_class =MsgSerializer
        pagination_class = None
        msg.objects

class TempDefineLast(ListCreateAPIView):
        queryset =temp.objects.all()
        serializer_class =TempSerializer
        pagination_class = None
        temp.objects

class MotorDefineLast(ListCreateAPIView):
        queryset =motor.objects.all()
        serializer_class =MotorSerializer
        pagination_class = None
        motor.objects
