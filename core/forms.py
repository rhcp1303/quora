from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Question, Answer, User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    pass

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'content': '',
        }