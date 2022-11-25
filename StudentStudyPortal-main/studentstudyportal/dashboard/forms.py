from typing import Text
from django import forms
from django.forms import fields, widgets
from . models import Notes,Homework,Todo,User
from django.contrib.auth.forms import UserCreationForm
# 1b1c1db5

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ["title","description"]

class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    
    class Meta:
        model = Homework
        widgets = {'due':widgets.DateInput(format=('%Y-%m-%d'))}
        fields = ['subject','title','description','due','is_finished']

class Dashboardform(forms.Form):
    text = forms.CharField(max_length=250,label="Enter your search here: " )


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']

    
class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input =  forms.CharField(label = False, required=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the number'}
    ))
    measure1 = forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input =  forms.CharField(label = False, required=False,widget=forms.TextInput(
        attrs = {'type':'number','placeholder':'Enter the number'}
    ))
    measure1 = forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='',widget=forms.Select(choices=CHOICES)
    )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','password1','password2']