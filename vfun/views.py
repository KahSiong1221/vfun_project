from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import SportsHall, Session
from .serializers import SportsHallSerializer, SessionSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SportsHallViewSet(viewsets.ModelViewSet):
    queryset = SportsHall.objects.all()
    serializer_class = SportsHallSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserSportsHallViewSet(viewsets.ModelViewSet):
    serializer_class = SportsHallSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user.username)
        return SportsHall.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
