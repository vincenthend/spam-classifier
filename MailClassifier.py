from MailData import MailData,MailDataLoader
import MailProcessor
import HTMLStripper

class classifier:
    def __init__(self,model):
        # Load trained model
        self.model = model

        # Load Testing mailData
        self.__mailDataTesting = MailDataLoader().loadTesting()

    def classify(self, mailDataTesting):
        # Preprocess mailDataTesting
        preprocessor = MailProcessor.Preprocessor()

        payload = []

        for mailData in self.__mailDataTesting:
            text = HTMLStripper.stripTags(mailData.payload)
            text = HTMLStripper.cleanText(text)
            payload.append(text)

        vector, dataset = preprocessor.preprocessData(payload)
        
        # predict mailDataTesting
        predicted = self.model.predict(dataset)

        # Get accuracy score
        print('Accuracy = %5.3f' % float(self.model.score(dataset,predicted)*100))
