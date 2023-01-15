from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_QM = models.BooleanField( 'QM status', default=False)
    is_QT = models.BooleanField('QT status', default=False)


#class CustomUser(AbstractUser):
    #QM = 1
    #QT = 2
    #ROLE_CHOICES = (
        #(QM, 'QM'),
        #(QT, 'QT'),
    #)
    #role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    number_of_questions = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    def get_questions(self):
        return self.question_set.all()

class Question(models.Model):
    content = models.CharField(max_length=300)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()
    
class Answer(models.Model):
    content = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"


class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.quiz)