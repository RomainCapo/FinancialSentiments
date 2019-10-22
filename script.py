from matplotlib import pyplot as plt

import pandas as pd
import numpy as np

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVR
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import en_core_web_sm
import spacy

dataset = pd.read_json('dataset/financialData.json')

X = dataset['title']
y = dataset['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

class TextProcessor(BaseEstimator, TransformerMixin):
    '''Class use in pipeline to processing the text'''
    def __init__(self, remove_stop_word=False, keep_only_good_word=True, min_word_size=2):
        '''Constructor of TextProcessor
        
        remove_stop_word=False -- remove stop word in the sentence
        keep_only_good_word=True -- keep only the verb, adverb, noun and adjectiv otherwise keep all the word type
        min_word_size=2 -- remove all the word smaller that min_word_size, -1 to ignore this param
        '''
        self.remove_stop_word = remove_stop_word
        self.keep_only_good_word = keep_only_good_word
        self.min_word_size = min_word_size
        self.good_words = ['VERB', 'ADV', 'NOUN', 'ADJ']
        self.nlp = spacy.load('en')
        self.punctuations = string.punctuation
        
    def spacy_text_processing(self, sentence):
        '''Process the sentence, Cut the sentence in word, according to the parameters : deletes the stop word, 
        keeps only or not the verbs, adjectives, noun and adverb, deletes the words below a certain size, 
        removes the punctuation, and keeps only the roots of the word.
        
        sentence -- sentence to transform
        '''
        final_sentence = []
        for word in self.nlp(sentence):
            if self.remove_stop_word:
                if word.is_stop:
                    continue
            
            if self.keep_only_good_word:
                if word.pos_ not in self.good_words:
                    continue
                    
            if self.min_word_size!=-1:
                if len(word.text) < self.min_word_size:
                    continue
                    
            if word.text not in self.punctuations:
                final_sentence.append(word.lemma_)
        return final_sentence
        
    def transform(self, X, y=None):
        '''Transform the text, call by the pipeline
        
        X -- data
        y=None -- labels of the data
        '''
        X_transformed = []
        for sentence in X:
            X_transformed.append(' '.join(self.spacy_text_processing(sentence)))
        return X_transformed
    
    def fit(self, X, y=None):
        '''Use for estimation
        
        X -- data
        y=None -- labels of the data
        '''
        return self

param_grid_rfr = {
    'text_processing__keep_only_good_word':(True, False), 
    'text_processing__remove_stop_word': (True, False),
    'text_processing__min_word_size' : [-1, 2,3,4,5],
    'tfidf__use_idf' : (True, False),
    'rfr__n_estimators' : [3,10,30],
    'rfr__max_features' : [2,4,6,8],
    'rfr__bootstrap' : (True, False)
}

rfr_grid_model = Pipeline([('text_processing', TextProcessor()),
                    ('vectorizer', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('rfr', RandomForestRegressor())])

random_search_rfr = RandomizedSearchCV(rfr_grid_model, param_grid_rfr,scoring='neg_mean_absolute_error',  n_iter=30, verbose=3, n_jobs=-1)
random_search_rfr.fit(X_train, y_train)

random_search_rfr.best_params_