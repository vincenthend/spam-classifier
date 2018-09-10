import sklearn.feature_extraction.text

class Preprocessor:
    # Constants
    minimalFreq = 0.01

    def preprocessData(self, data):
        self.vector = sklearn.feature_extraction.text.CountVectorizer(stop_words = 'english', token_pattern=r"\b[A-Za-z][A-Za-z]+\b", min_df=self.minimalFreq)
        train_count = self.vector.fit_transform(data)
        transformer = sklearn.feature_extraction.text.TfidfTransformer()
        train_tf = transformer.fit_transform(train_count)
        return train_tf
    
    def getCountVectorizer(self):
        return self.vector
