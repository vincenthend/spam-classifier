from MailData import MailData
import sklearn

class Preprocessor:
    # List of stopwords
    __stopwords = []

    # return sklearn.feature_extraction.text.CountVectorizer
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
    def Train(self, mailDataList):
        # Implement training, use tenfold to get training accuracy
        preprocessor = Preprocessor()
        
        payloads = []
        label = []
        for mailData in mailDataList:
            payloads.append(mailData.payload)
            label.append(mailData.label)
        
        features = preprocessor.preprocessData(payloads)
        model = self.__trainKnn(features, label)
            
    def __trainKnn(self, features, label):
        classifier = sklearn.neighbors.KNeighborsClassifier()
        classifier.fit(features, label)

        return classifier

    def Save(self, fileName):
        # Save trained data, retrain to make sure data has been trained
        pass