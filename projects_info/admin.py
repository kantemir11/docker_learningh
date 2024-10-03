from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import ProjectsInfo, Technologies, MyInfo


@admin.register(ProjectsInfo)
class ProjectsInfoAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    group_fieldsets= True
    list_display = ("name", "it_field", "my_order")

@admin.register(Technologies)
class TechnologiesAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(MyInfo)
class MyInfoAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
