from MailData import MailData,MailDataLoader
import MailProcessor
import HTMLStripper

class classifier:
    def __init__(self):
        # Load trained model

        # Load Testing mailData
        self.mailDataTesting = <ailDataLoader.loadTesting()
    
    def classify(self, model, mailDataTesting):
        # Preprocess mailDataTesting
        preprocessor = MailProcessor.Preprocessor();

        payload = []

        for mailData in mailDataTesting:
            text = HTMLStripper.stripTags(mailData.payload)
            text = HTMLStripper.cleanText(text)
            payload.append(text)

        
        pass 

    