from MqttApp.models import *
from rest_framework import serializers 

class PresionSerializer(serializers.ModelSerializer):
    class Meta:
        model = presion
        fields = ('id',
                  'pub_date',
                  'value',
                  )

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = action
        fields = ('id',
                  'pub_date',
                  'value',
                  )

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = action
        fields = ('id',
                  'pub_date',
                  'value',
                  )

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = action
        fields = ('id',
                  'pub_date',
                  'value',
                  )
class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = motor
        fields = ('id',
                  'pub_date',
                  'value',
                  'cmdfromapp',
                  )