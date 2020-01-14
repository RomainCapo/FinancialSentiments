from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer

class SentenceVectorizer(BaseEstimator, TransformerMixin):
    def __init__(self, max_sentence_length, w2vec_model):

        self.max_sentence_length = max_sentence_length
        self.X_train = X_train
        self.X_test = X_test
        self.w2vec_model = w2vec_model
        

    def compute_tfidf(X):
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(X)

        feature_names = tfidf.get_feature_names()
        return dict(zip(feature_names, tfidf.idf_))

    def get_tfidf_score(self, word):
        '''Return the TF-idf score for a word. If the word is not in the dict return 0.
        
        word -- a word of a sentence
        
        return -- the TF-idf score for this word
        '''
        if word in word2tfidf:
            return word2tfidf[word]
        else:
            return 0.0

    def get_w2v_from_word(word, dimension=100):
    '''Return the word2vec vector for the given word. 
    If the word is not in the word2vec vocab return a fille vector of 0 the size of the dimension
    
    word -- a word of a sentence
    dimension -- the dimension of the vector
    
    return -- The word2vec vector
    '''
    if word in self.w2vec_model.wv.vocab: 
        doc = trigram_mod[bigram_mod[[word]]]
        return self.w2vec_model.wv[doc][0]
    else :
        return np.zeros(dimension)