from django.contrib import admin
from .models import Quiz, Question, Answer, Marks_Of_User, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

admin.site.register(Quiz)

class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Role',
            {
                'fields':(
                    'is_QM',
                    'is_QT',
                )
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Marks_Of_User)
