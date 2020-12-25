from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question Information",              {'fields':['question_text']}),
        ("Date Information",{'fields':['pub_date'],'classes':['collapse']})
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date')
admin.site.register(Question,QuestionAdmin)