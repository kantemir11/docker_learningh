from django.db import models

# Create your models here.
class ProjectsInfo(models.Model):
    name=models.CharField(max_length=150, blank=True, null=True)
    it_field = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default='')
    github = models.CharField(max_length=200, default='')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta:
        ordering = ['my_order']
        verbose_name = "Информация о проекте"
        verbose_name_plural = "Информация о пректах"

class Technologies(models.Model):
    project = models.ManyToManyField(ProjectsInfo, related_name='technologies')
    technology_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default='')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta:
        ordering = ['my_order']
        verbose_name = "Технология"
        verbose_name_plural = "Технологии"


class MyInfo(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True )
    email = models.CharField(max_length=150, blank=True, null=True)
    linkedin = models.CharField(max_length=150,blank=True, null=True )
    github = models.CharField(max_length=150, blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta:
        ordering = ['my_order']
        verbose_name = "Моя информация"
        verbose_name_plural = "Моя информация"


