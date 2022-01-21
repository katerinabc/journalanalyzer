#from django.forms import ModelForm #uncomment this as the next line imports ModelForm together with forms
from django import forms
from journal.models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description')

class EntryFormSimple(forms.Form):
    description = forms.CharField(label="Your Journal Entry", widget=forms.Textarea)
