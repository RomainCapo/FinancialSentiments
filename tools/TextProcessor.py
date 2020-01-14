from sklearn.base import BaseEstimator, TransformerMixin
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import en_core_web_sm
import string
import spacy

nlp = spacy.load('en')
class TextProcessor(BaseEstimator, TransformerMixin):
    '''Class use in pipeline to processing the text'''
    def __init__(self, remove_stop_word=False, keep_only_good_word=True, min_word_size=2, is_word_joined=True):
        '''Constructor of TextProcessor
        
        remove_stop_word=False -- remove stop word in the sentence
        keep_only_good_word=True -- keep only the verb, adverb, noun and adjectiv otherwise keep all the word type
        min_word_size=2 -- remove all the word smaller that min_word_size, -1 to ignore this param
        '''
        self.remove_stop_word = remove_stop_word
        self.keep_only_good_word = keep_only_good_word
        self.min_word_size = min_word_size
        self.good_words = ['VERB', 'ADV', 'NOUN', 'ADJ']
        self.is_word_joined = is_word_joined
        self.vocab = set()
        
        self.punctuations = string.punctuation
        
    def spacy_text_processing(self, sentence):
        '''Process the sentence, Cut the sentence in word, according to the parameters : deletes the stop word, 
        keeps only or not the verbs, adjectives, noun and adverb, deletes the words below a certain size, 
        removes the punctuation, and keeps only the roots of the word.
        
        sentence -- sentence to transform
        '''
        final_sentence = []
        for word in nlp(sentence):
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
                self.vocab.add(word.lemma_)
        return final_sentence
        
    def transform(self, X, y=None):
        '''Transform the text, call by the pipeline
        
        X -- data
        y=None -- labels of the data
        '''
        X_transformed = []
        for sentence in X:
            if self.is_word_joined:
                X_transformed.append(' '.join(self.spacy_text_processing(sentence)))
            else : 
                X_transformed.append(self.spacy_text_processing(sentence))
        return X_transformed
    
    def fit(self, X, y=None):
        '''Use for estimation
        
        X -- data
        y=None -- labels of the data
        '''
        return self