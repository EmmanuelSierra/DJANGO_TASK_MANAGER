from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput
from .models import Task


# (Model-form) Create Register a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# (Model-form) Authenticate to login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# (Model-form) CRUD Tasks
class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Add a new task'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Description'}))

    class Meta:
        model = Task
        fields = "__all__"
