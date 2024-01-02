from datetime import datetime

from django.contrib.auth.models import User
from .models import SportsHall, Session, Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_no']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile']


class SportsHallSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = SportsHall
        fields = ['id', 'name', 'address', 'location', 'courts', 'phone_no', 'created_by']


class ActiveSessionSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(datetime__gte=datetime.now())
        return super(ActiveSessionSerializer, self).to_representation(data)


class SessionSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Session
        list_serializer_class = ActiveSessionSerializer
        fields = '__all__'
