from django.shortcuts import render, redirect
from journal.models import Entry
#from journal.forms import EntryForm
from journal.forms import EntryFormSimple
#from journal import forms
from django.template.defaultfilters import slugify
from django.db.models import Count

from journal import sentiment_analysis # I made this part of journal.model, but wondering if it shouldn't be part of another app?

def index(request):

    form_class= EntryFormSimple

    if request.method == 'POST':
        form = form_class(request.POST) # create from instance. form_class is defined above. An alternative is to write form = EntryFormSimple(request.POST)

        if form.is_valid():
            entry = form.cleaned_data
            description = entry['description']
            wcount  = sentiment_analysis.wordcount(form.cleaned_data['description'])
            ressentiment = sentiment_analysis.sentiment(form.cleaned_data['description'])

            context = {
                'form':form, # I needed to add this to show the form
                'description': entry,
                'wcount': wcount,
                'sentiment': ressentiment,
            }
            return render (request, 'index.html', context)

    else:
        form = EntryFormSimple()


    return render (request, 'index.html', {'form':form})



# def index(request):
# this was my first attempt at creating the form.
# what worked: putting the data in and sending it to the text Analyzer
# what did not work: displaying the original input together with the
# emotional score.
#     form_class = EntryForm
#
#     # if we're coming from a submitted form, do this
#     if request.method == 'POST':
#         # grab the data from the submitted form and
#         # apply to the form
#         form = form_class(request.POST)
#         if form.is_valid():
#             # create an instance but don't save yet
#             entry = form.save(commit=False)
#
#             # set the additional details
#             #thing.user = request.user
#             entry.slug = slugify(entry.title)
#             #entry.wcount = wordcount(entry.description)
#
#             #text = request.POST.get('newentry')['description'] # linked to form on create_entry page
#             text = entry.description
#             #print(text)
#             wcount  = sentiment_analysis.wordcount(text)
#             entry.wcount = wcount
#
#             ressentiment = sentiment_analysis.sentiment(text)
#             entry.sentiment = ressentiment
#             #conf = conf*100
#             context = {
#                 'entry': entry,
#                 'wcount': wcount,
#                 'slug': entry.slug,
#                 'sentiment': ressentiment,
#                 #'confidence': conf,
#                 }
#
#             # save the object
#             entry.save()
#
#             # redirect to our newly created thing
#             return render(request, 'index.html', context)
#
#     # otherwise just create the form
#     else:
#         form = form_class()
#
#
#     #context = {}
#     return render(request, 'index.html', {
#         'form':form
#     })


# def index(request):
#     #entries = Entry.objects.filter(description__contains='rejected') # change this to decide how to query for something
#     entrys = Entry.objects.all() # returns all objects. slows down website
#     return render(request, 'index.html', {
#         'entrys': entrys,
#     })
#
#
# def entry_detail(request, slug):
#     # grap the objects
#     entry = Entry.objects.get(slug = slug) # here entry is in singular because only show 1 entry. in the index page show all entries
#
#     # and pass to the template
#     return render(request, 'entrys/entry_detail.html', {
#         'entry':entry,
#     })
#
# def edit_entry(request, slug):
#     #grap the objects
#     entry = Entry.objects.get(slug = slug)
#     # set the forms view we are using
#     form_class = EntryForm
#
#     # if we're coming to this view from a submitted form
#     if request.method == 'POST':
#         # grab the data from the submitted form and apply to
#         # the form
#         form = form_class(data=request.POST, instance=entry)
#         if form.is_valid():
#             # save the new data
#             form.save()
#             return redirect('entry_detail', slug=entry.slug)
#     # otherwise just create the form
#     else:
#         form = form_class(instance=entry)
#
#     #and render the template
#     return render(request, 'entrys/edit_entry.html', {
#         'entry':entry,
#         'form': form,
#     })
