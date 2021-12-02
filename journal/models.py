from django.db import models
from django.contrib.auth.models import AbstractUser

# for text analysis
#import nltk
#from nltk.util import ngrams, word_tokenize, bigrams, trigrams

# Create your models here.

class User(AbstractUser):
    pass

class Entry(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    wcount = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    sentiment = models.DecimalField(max_digits=4, decimal_places=0, blank = True, null = True)

    # def __str__(self):
    #     return str(self.name)
    #sentiment_score = models.DecimalField(max_digits=2, decimal_places=1)

   #  def is_critical(self):
   #     return True if sentiment_score.score < -0.2 else False
   #
   # def __str__(self):
   #     return self.title

    #begin easy: count number of words in text entry

class words(models.Model):
    title = models.OneToOneField(Entry, on_delete=models.CASCADE, primary_key=True)
    word = models.TextField()
    #add relationship that title here is part of title in the other
