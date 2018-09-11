import sklearn.feature_extraction.text
from nltk.tokenize import *
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class Preprocessor:
    # Constants
    minimalFreq = 0.01

    def preprocessData(self, data):
        messages = [self.__processText(d) for d in data]
        
        vector = CountVectorizer(stop_words = 'english', min_df=self.minimalFreq)
        train_count = vector.fit_transform(messages)
        transformer = sklearn.feature_extraction.text.TfidfTransformer()
        train_tf = transformer.fit_transform(train_count)
        print(vector.get_feature_names())
        return vector, train_tf

        

    def __processText(self, text):
        # Lowercase, tokenize
        text = text.lower()
        token = word_tokenize(text)
        token = [t for t in token if len(t) >= 3]

        # Remove Stopwords
        stops = stopwords.words('english')
        token = [t for t in token if t not in stops]
        
        # Stemmer
        stemmer = PorterStemmer()
        token = [stemmer.stem(t) for t in token]
        
        token = ' '.join(token)
        return token

