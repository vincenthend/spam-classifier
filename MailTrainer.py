from MailData import MailData,MailDataLoader
import HTMLStripper
import MailProcessor
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

class Trainer:
    # Constants
    test_size = 0.4

    def __init__(self, classifier):
        self.classifier = classifier

    def train(self, mailDataList):
        preprocessor = MailProcessor.Preprocessor()
        
        payloads = []
        label = []
        for mailData in mailDataList:
            text = HTMLStripper.stripTags(mailData.payload)
            text = HTMLStripper.cleanText(text)
            payloads.append(text)
            label.append(mailData.label)

        self.vector, dataset = preprocessor.preprocessData(payloads)
        self.__trainModel(dataset, label)
            
    def __trainModel(self, data, label):
        X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=self.test_size, random_state=0,shuffle=True)

        self.classifier.fit(X_train, y_train)
        print('Accuracy : %5.3f' % float(self.classifier.score(X_test, y_test)*100))

    def save(self, fileName):
        # Save trained data, retrain to make sure data has been trained
        pass

    def getVectorCount(self):
        return self.vector

if __name__ == "__main__":
    data = MailDataLoader().loadTraining()
    #classifier = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(300, 10), random_state=1)
    #classifier = KNeighborsClassifier(n_neighbors=50)
    #classifier = svm.SVC()
    classifier = MultinomialNB()

    trainer = Trainer(classifier)
    trainer.train(data)
    print('Feature count :', len(trainer.getVectorCount().get_feature_names()))