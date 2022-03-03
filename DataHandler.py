import requests
import json

class DataHandler:

    def __init__(self,folderPath = ""):
        self.__folderPath = folderPath
        self.__possibleCats = ["Location","Room","Food","Staff","ReasonForStay", "GeneralUtility","HotelOrganisation", "Unknown"]


    def getScoreData(self):
        scoreData = []
        if len(self.__folderPath) == 0:
            response = self.__getDataFromServer()
            reviews = response['data']['Reviews']
            for revKey in reviews.keys():
                sentences = reviews[revKey]['Sentences']
                for senKey in sentences.keys():
                    classifications = sentences[senKey]['Classifications']
                    scoreData.append([sentences[senKey]['Sentence'],classifications[list(classifications.keys())[0]]["Score"]])
        else:
            response = self.__getDataFromFiles()
            print(response)
        return scoreData

    def getContentTypeData(self):
        contentTypeData = []
        if len(self.__folderPath) == 0:
            response = self.__getDataFromServer()
            reviews = response['data']['Reviews']
            for revKey in reviews.keys():
                sentences = reviews[revKey]['Sentences']
                for senKey in sentences.keys():
                    classifications = sentences[senKey]['Classifications']
                    contentTypeData.append([sentences[senKey]['Sentence'],
                                      classifications[list(classifications.keys())[0]]["ContentType"]])
        return contentTypeData


    def getCategorieData(self,cat):
        if cat not in self.__possibleCats:
            print("----\u001b[1m\u001b[31;1mThis Categorie does not exists\u001b[0m\n----will return only the first Categorie, may case unwanted results\u001b[0m")
        categorieData = []
        if len(self.__folderPath) == 0:
            response = self.__getDataFromServer()
            reviews = response['data']['Reviews']
            for revKey in reviews.keys():
                sentences = reviews[revKey]['Sentences']
                for senKey in sentences.keys():
                    classifications = sentences[senKey]['Classifications']
                    listOfPossibleClassification = []
                    for classificationKey in classifications.keys():
                        listOfPossibleClassification.append(classifications[classificationKey]["Classification"])

                    if cat in listOfPossibleClassification :
                        categorieData.append([sentences[senKey]['Sentence'],cat])
                    else:
                        categorieData.append([sentences[senKey]['Sentence'], listOfPossibleClassification[0]])
        return categorieData


    def __getDataFromServer(self):
        url = "http://152.96.24.231:81/backend/getAllData"
        response = requests.request("GET", url)
        return json.loads(response.text)


    def __getDataFromFiles(self):
        sentencesAsList = []
        with open(self.__folderPath +"/ReviewSentences.tsv") as sentencesFile:
            sentencesAsList = [sen.split('\t')[0] for sen in sentencesFile.read().split('\n')]

        classificationAsList = []
        with open(self.__folderPath +"/ClassificationResult.tsv")as classificationFile:
            classificationAsList = [[classification.split('\t')[0],classification.split('\t')[2],classification.split('\t')[4],classification.split('\t')[6]] for classification in classificationFile.read().split('\n')]

        return classificationAsList

