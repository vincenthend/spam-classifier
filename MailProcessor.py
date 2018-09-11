import sklearn.feature_extraction.text
from nltk.tokenize import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Preprocessor:
    # Constants
    minimalFreq = 1

    def preprocessData(self, data):
        messages = [self.__processText(d) for d in data]
        
        vector = CountVectorizer(stop_words = 'english', min_df=self.minimalFreq)
        train_count = vector.fit_transform(messages)
        transformer = sklearn.feature_extraction.text.TfidfTransformer()
        train_tf = transformer.fit_transform(train_count)
        print(vector.get_feature_names())
        return vector, train_tf

        

    def __processText(self, text, use_tokenize=True, use_stopwords=True, use_stemmer=True):
        # Lowercase
        text = text.lower()

        # Tokenize
        if(use_tokenize):
            token = word_tokenize(text)
            token = [t for t in token if len(t) >= 3]

        # Remove Stopwords
        if(use_stopwords):
            stops = stopwords.words('english')
            token = [t for t in token if t not in stops]
        
        # Stemmer
        if(use_stemmer):
            lemma = WordNetLemmatizer()
            token = [lemma.lemmatize(t) for t in token]
        
        if(use_tokenize):
            text = ' '.join(token)
        return text