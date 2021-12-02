from django.shortcuts import render, redirect
from journal.models import Entry
from journal.forms import EntryForm
from django.template.defaultfilters import slugify
from django.db.models import Count

from journal import sentiment_analysis # I made this part of journal.model, but wondering if it shouldn't be part of another app?


#import nltk
#https://stackoverflow.com/questions/42193818/using-nltk-inside-django-app

# def Wordcount(description):
#     entry = Entry.objects.all
#     word = entry.split(" ")
#     wcount = Counter(words)
#     return wcount


def index(request):
    #entries = Entry.objects.filter(description__contains='rejected') # change this to decide how to query for something
    entrys = Entry.objects.all() # returns all objects. slows down website
    return render(request, 'index.html', {
        'entrys': entrys,
    })


def entry_detail(request, slug):
    # grap the objects
    entry = Entry.objects.get(slug = slug) # here entry is in singular because only show 1 entry. in the index page show all entries

    # and pass to the template
    return render(request, 'entrys/entry_detail.html', {
        'entry':entry,
    })

def edit_entry(request, slug):
    #grap the objects
    entry = Entry.objects.get(slug = slug)
    # set the forms view we are using
    form_class = EntryForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=entry)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('entry_detail', slug=entry.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=entry)

    #and render the template
    return render(request, 'entrys/edit_entry.html', {
        'entry':entry,
        'form': form,
    })

def create_entry(request):
    form_class = EntryForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            entry = form.save(commit=False)

            # set the additional details
            #thing.user = request.user
            entry.slug = slugify(entry.title)
            #entry.wcount = wordcount(entry.description)

            #text = request.POST.get('newentry')['description'] # linked to form on create_entry page
            text = entry.description
            #print(text)
            wcount  = sentiment_analysis.wordcount(text)
            entry.wcount = wcount

            ressentiment = sentiment_analysis.sentiment(text)
            entry.sentiment = ressentiment
            #conf = conf*100
            # context = {
            #     'text': text,
            #     'wcount': wcount,
            #     'slug': entry.slug,
            #     #'confidence': conf,
            #     }

            # save the object
            entry.save()

            # redirect to our newly created thing
            return redirect('entry_detail', slug=entry.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'entrys/create_entry.html', {
        'form': form,
    })

# this is the view of the sentiment analysis. I want it to also show on the create_entry page. Does it have to be part of the other view? So one view statement per page?
# def create_entry(request):
#
#     # logic
#     if request.method == 'POST':
#         text = request.POST.get('newentry') # linked to form on create_entry page
#         res  = sentiment_analysis.sentiment(text)
#         #conf = conf*100
#         context = {
#             'text': text,
#             'count': wcount,
#             #'confidence': conf,
#         }
#         return render(request, 'entrys/create_entry.html', context)
#
#     context = {}
#     return render(request, 'entrys/create_entry.html', context)
