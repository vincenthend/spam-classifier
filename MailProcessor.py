from MailData import MailData
import sklearn

class Preprocessor:
    # List of stopwords
    __stopwords = []

    # Preprocess data
    def preprocessData(self, data):
        self.__tokenize(data)
        self.__removeStopwords(data)

    def __tokenize(self, data):
        # Implement tokenizer
        pass # Please remove these

    def __removeStopwords(self, text):
        # Implement remove stopwords
        pass

class Trainer:
    def Train(self, MailDataList):
        # Implement training, use tenfold to get training accuracy
        pass

    def Save(self, fileName):
        # Save trained data, retrain to make sure data has been trained
        pass