from MailData import MailData,MailDataLoader
import HTMLStripper
import sklearn.neighbors
import MailProcessor
from sklearn.model_selection import train_test_split

class Trainer:
    # Constants
    test_size = 0.2

    def __init__(self, classifier):
        self.classifier = classifier

    def train(self, mailDataList):
        preprocessor = MailProcessor.Preprocessor()
        
        payloads = []
        label = []
        for mailData in mailDataList:
            payloads.append(HTMLStripper.stripTags(mailData.payload))
            label.append(mailData.label)

        dataset = preprocessor.preprocessData(payloads)
        self.__trainModel(dataset, label)
            
    def __trainModel(self, data, label):
        X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=self.test_size, random_state=0)

        self.classifier.fit(X_train, y_train)
        print(self.classifier.score(X_test, y_test))

    def save(self, fileName):
        # Save trained data, retrain to make sure data has been trained
        pass

if __name__ == "__main__":
    data = MailDataLoader().loadTraining()

    trainer = Trainer(sklearn.neighbors.KNeighborsClassifier(n_neighbors=5))
    trainer.train(data)