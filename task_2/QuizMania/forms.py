from django import forms
from .models import Quiz, Question, Answer, CustomUser
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'description', 'number_of_questions')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', 'quiz')

#I have no idea why this is working but I'm not touching anything
class CustomUserCreationForm(UserCreationForm):
    ROLES = ['QM', 'QT']
    role = forms.ChoiceField(choices=ROLES, required=True)     
              
    class Meta(UserCreationForm.Meta):
        model = CustomUser

        def save(self, commit=True):
            user = super().save(commit=False)
            if user.role == 'QM':
                user.is_QM = True
            else:
                user.is_QT = True

            if commit:
                user.save()
            
            return user

            #fields = ('username', 'email', 'password1', 'password2')