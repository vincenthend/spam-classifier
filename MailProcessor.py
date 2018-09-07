from MailData import MailData
import sklearn

class Preprocessor:
    # List of stopwords
    __stopwords = []

    # Preprocess data
    def preprocessData(self, data):
        vector = CountVectorizer()
        train_count = vector.fit_transform(loadTraining())
        transformer = TfidfTransformer()
        train_tf = transformer.fit_transform(train_count)
        return train_tf

class Trainer:
    def Train(self, MailDataList):
        # Implement training, use tenfold to get training accuracy
        pass

    def Save(self, fileName):
        # Save trained data, retrain to make sure data has been trained
        pass