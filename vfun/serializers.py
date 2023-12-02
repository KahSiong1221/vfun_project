from .models import SportsHall
from rest_framework import serializers


class SportsHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsHall
        fields = ("id", "hall_name", "address", "location", "courts", "phone_no", "created_by")
