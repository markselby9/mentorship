from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mentor_server.mentor.serializers import UserSerializer, GroupSerializer, MentorSerializer
from models import Mentor


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class MentorViewSet(viewsets.ModelViewSet):
  queryset = Mentor.objects.all()
  serializer_class = MentorSerializer
