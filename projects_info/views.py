from rest_framework.mixins import (CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet
from .serializers import ProjectsInfoSerializer, TechnologiesSerializer, MyInfoSerializer
from rest_framework.permissions import IsAuthenticated

from .models import ProjectsInfo, Technologies, MyInfo

class ProjectsInfoViewSet(GenericViewSet, CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
      serializer_class = ProjectsInfoSerializer
      queryset = ProjectsInfo.objects.all()
      permission_classes = (IsAuthenticated,)


class TechnologiesViewSet(GenericViewSet, CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
      serializer_class = TechnologiesSerializer
      queryset = Technologies.objects.all()
      permission_classes = (IsAuthenticated,)


class MyInfoViewSet(GenericViewSet, CreateModelMixin,ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
      serializer_class = MyInfoSerializer
      queryset = MyInfo.objects.all()
      permission_classes = (IsAuthenticated,)
