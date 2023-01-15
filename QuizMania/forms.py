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

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')