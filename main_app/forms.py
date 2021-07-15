# from typing_extensions import Required
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import Proposal, Activity, Comment

from django.forms.widgets import TextInput

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category', 'date', 'duration', 'start', 'location', 'attendees']
        widgets = {
            'date': forms.DateInput(format=('%m-%d-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{2}-\d{2}-\d{4}', 'lang': 'pl', 'format': 'mm-dd-YYYY', 'type': 'date'},),
            'duration': TextInput(attrs={'placeholder': '00 day 00:00:00'}),
            'start': forms.TimeInput(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['attendees'].required = False

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['location', 'suggestion']
    labels = {
      'location': (''),
      'suggestion': (''),
    }
    widgets = {
      'suggestion': forms.Textarea(attrs={"rows":2, 'placeholder':'add any additional info here', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'}),
      'location': forms.Textarea(attrs={"rows":2,'placeholder':'add location preference here - helpful to include city ', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'})
    }

class ProposalUpdateForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['location', 'suggestion']
    labels = {
      'location': (''),
      'suggestion': (''),
    }
    widgets = {
      'suggestion': forms.Textarea(attrs={"rows":2, 'placeholder':'add any additional info here', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'}),
      'location': forms.Textarea(attrs={"rows":2,'placeholder':'add location preference here - helpful to include city ', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'})
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    labels = {
      'content': ('')
    }
    widgets = {
      'content': forms.Textarea(attrs={"rows":5, 'placeholder':'add comment here', 'style': 'border-radius: 30px', 'class': 'comment-text-box'}),
    } 