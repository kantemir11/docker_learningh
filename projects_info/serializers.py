from rest_framework.serializers import ModelSerializer

from .models import ProjectsInfo, Technologies, MyInfo


class ProjectsInfoSerializer(ModelSerializer):
    class Meta:
        model = ProjectsInfo
        fields = ['name', 'it_field']


class TechnologiesSerializer(ModelSerializer):
    class Meta:
        model = Technologies
        fields = ['project', 'technology_name']


class MyInfoSerializer(ModelSerializer):
    class Meta:
        model = MyInfo
        fields = ['phone_number', 'email', 'linkedin', 'github']