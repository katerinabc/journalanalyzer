from django.forms import ModelForm

from journal.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'description')
