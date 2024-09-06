from django import forms
from .models import Answer
from django.contrib.auth.models import User
from codemirror2.widgets import CodeMirrorEditor

class YourForm(forms.Form):
    code = forms.CharField(widget=CodeMirrorEditor(options={'mode': 'python'}))



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('author', 'task', 'code')

class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

class PfpForm(forms.Form):
    pfp = forms.ImageField(allow_empty_file=False)