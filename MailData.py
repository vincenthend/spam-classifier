import os, csv
import ast

# Class MailData, contains method for creating email
class MailData:
    def __init__(self, subject, body, label=None):
        self.payload = subject + " " + body
        self.label = label

# Class MailLoader, loads text file and turn it into MailData object
class MailDataLoader:
    __trainingPath = "data/TR"
    __testingPath = "data/TT"
    __trainingLabel = "spam-mail.tr.label"

    def __loadFolder(self, folderName):
        if os.path.exists(folderName):
            files = os.listdir(folderName)
            mailData = []
            for file in files:
                srcpath = os.path.join(folderName, file)

                mailFile = open(srcpath,"r")
                mail = ast.literal_eval(mailFile.read())
                mailData.append(MailData(mail["subject"],mail["body"]))
                mailFile.close()
        else:
            raise ValueError("Folder does not exist")
        return mailData

    def loadTraining(self):
        trainingData = self.__loadFolder(self.__trainingPath)
        labels = list(csv.reader(open(self.__trainingLabel,"r")))
        for label in labels:
            if(label[0] != 'Id'):
                trainingData[int(label[0])-1].label = bool(int(label[1]))

        return trainingData

    def loadTesting(self):
        return self.__loadFolder(self.__trainingPath)


if __name__ == "__main__":
    builder = MailDataLoader()

    trainingData = builder.loadTraining()
    print(trainingData[3].label)