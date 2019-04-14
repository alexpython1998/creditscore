from django.contrib import admin
from .models import Choice, Poll, Question, UserPolls, Advice
# Register your models here.


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'score')


class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ('choices',)

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(UserPolls)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll)
admin.site.register(Advice)