#sentiment sentiment_analysis
import nltk
import random
import pickle
import os
from journalapp.settings import BASE_DIR

from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI
from nltk.sentiment import SentimentIntensityAnalyzer

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from statistics import mode
from collections import Counter

# def sentiment(text):
#     feats = text.strip(" ")
#     wcount = Counter(feats)
#     return wcount

def wordcount(text):
    mystring = word_tokenize(text)
    wcount = len(mystring)
    return wcount

def sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    res = sentiment['compound']
    res = (res*100)
    return res
















# class VoteClassifier(ClassifierI):
#     def __init__(self, *classifiers):
#         self._classifiers = classifiers
#
#     def classify(self, features):
#         votes = []
#         for c in self._classifiers:
#             v = c.classify(features)
#             votes.append(v)
#         return mode(votes)
#
#     def confidence(self, features):
#         votes = []
#         for c in self._classifiers:
#             v = c.classify(features)
#             votes.append(v)
#         choice_votes = votes.count(mode(votes))
#         conf = choice_votes / len(votes)
#         return conf
#
#
# PICKLED_PATH = os.path.join(BASE_DIR, 'journal', 'pickled_files')
#
# path = os.path.join(PICKLED_PATH, 'documents.pickle')
# documents_f = open(path, "rb")
# documents = pickle.load(documents_f)
# documents_f.close()
#
# # word_features5k_f = open("pickled_files/word_features5k.pickle", "rb")
# path = os.path.join(PICKLED_PATH, 'word_features5k.pickle')
# word_features5k_f = open(path, "rb")
# word_features = pickle.load(word_features5k_f)
# word_features5k_f.close()
#
#
# def find_features(document):
#     words = word_tokenize(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#
#     return features
#
# path = os.path.join(PICKLED_PATH, 'featuresets.pickle')
# featuresets_f = open(path, "rb")
# featuresets = pickle.load(featuresets_f)
# featuresets_f.close()
#
# random.shuffle(featuresets)
# # print(len(featuresets))
#
# testing_set = featuresets[10000:]
# training_set = featuresets[:10000]
#
# path = os.path.join(PICKLED_PATH, 'originalnaivebayes5k.pickle')
# open_file = open(path, "rb")
# classifier = pickle.load(open_file)
# open_file.close()
#
# path = os.path.join(PICKLED_PATH, 'MNB_classifier5k.pickle')
# open_file = open(path, "rb")
# MNB_classifier = pickle.load(open_file)
# open_file.close()
#
# path = os.path.join(PICKLED_PATH, 'BernoulliNB_classifier5k.pickle')
# open_file = open(path, "rb")
# BernoulliNB_classifier = pickle.load(open_file)
# open_file.close()
#
# path = os.path.join(PICKLED_PATH, 'LogisticRegression_classifier5k.pickle')
# open_file = open(path, "rb")
# LogisticRegression_classifier = pickle.load(open_file)
# open_file.close()
#
# path = os.path.join(PICKLED_PATH, 'LinearSVC_classifier5k.pickle')
# open_file = open(path, "rb")
# LinearSVC_classifier = pickle.load(open_file)
# open_file.close()
#
# path = os.path.join(PICKLED_PATH, 'SGDC_classifier5k.pickle')
# open_file = open(path, "rb")
# SGDC_classifier = pickle.load(open_file)
# open_file.close()
#
#
# voted_classifier = VoteClassifier(
#   classifier,
#   LinearSVC_classifier,
#   MNB_classifier,
#   BernoulliNB_classifier,
#   LogisticRegression_classifier)
#
# def sentiment(text):
#     feats = find_features(text)
#     return voted_classifier.classify(feats),voted_classifier.confidence(feats)
