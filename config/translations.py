from modeltranslation.translator import register, TranslationOptions, translator
from apps.models import User


# @register(User)
class Usertans(TranslationOptions):
    fields = ('name', 'lastname', 'username')


translator.register(User, Usertans)
