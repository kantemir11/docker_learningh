from modeltranslation.translator import TranslationOptions, register

from .models import ProjectsInfo, Technologies, MyInfo


@register(ProjectsInfo)
class ProjectsInfoTranslationOptions(TranslationOptions):
    fields = ('name', 'it_field', )

@register(Technologies)
class TechnologiesTranslationOptions(TranslationOptions):
    fields = ('project', 'technology_name', )

