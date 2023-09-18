from modeltranslation.translator import  TranslationOptions, register
from .models import  Todo

@register(Todo)
class TodoTranslationOptions(TranslationOptions):
    fields = ('title',)

# translator.register(Todo, TodoTranslationOptions)