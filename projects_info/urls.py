from django.urls import include, path
from rest_framework import routers
from .views import ProjectsInfoViewSet, TechnologiesViewSet, MyInfoViewSet

projects_info = routers.DefaultRouter()
projects_info.register(r'projects_info', ProjectsInfoViewSet, basename='projects_info')

technologies = routers.DefaultRouter()
technologies.register(r'technologies', TechnologiesViewSet, basename='technologies')

my_info = routers.DefaultRouter()
my_info.register(r'my_info', MyInfoViewSet, basename='my_info')


urlpatterns = [
    path('', include(projects_info.urls)),
    path('projects_info/<int:pk>/', ProjectsInfoViewSet.as_view, name="projects_info"),
    path('technologies/<int:pk>/', TechnologiesViewSet.as_view, name="technologies"),
    path('my_info/<int:pk>/', MyInfoViewSet.as_view, name="my_info"),
]