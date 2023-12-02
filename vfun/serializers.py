from .models import Profile, SportsHall, Session
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "phone_no")


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("id", "hall", "organizer", "datetime", "duration_min", "capacity", "level", "gender", "players", "price")


class SportsHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsHall
        fields = ("id", "hall_name", "address", "location", "courts", "phone_no", "created_by")
