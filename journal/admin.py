from django.contrib import admin
from journal.models import Entry # import my model

class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug':('title',)}




# Register your models here.
admin.site.register(Entry, EntryAdmin) # register model
