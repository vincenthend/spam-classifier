from MailData import MailData,MailDataLoader
import sklearn
import sklearn.feature_extraction.text

class Preprocessor:
    # List of stopwords
    __stopwords = []

    # return sklearn.feature_extraction.text.CountVectorizer
    # Preprocess data
    def preprocessData(self, data):
        vector = sklearn.feature_extraction.text.CountVectorizer(stop_words = 'english')
        train_count = vector.fit_transform(data)
        transformer = sklearn.feature_extraction.text.TfidfTransformer()
        train_tf = transformer.fit_transform(train_count)
        return train_tf

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

if __name__ == "__main__":
    trainer = Trainer()
    
    data = MailDataLoader().loadTraining()
    trainer.Train(data)