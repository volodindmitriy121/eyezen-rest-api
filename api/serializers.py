from rest_framework import serializers

from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email', 'number', 'user_type')


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('url', 'id', 'type', 'status')


class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = ('url', 'id', 'square', 'sensor', 'user')
