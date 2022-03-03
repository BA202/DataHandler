from DataHandler.DataHandler import DataHandler


myDataHandler = DataHandler("/Users/tobiasrothlin/Documents/BachelorArbeit/DataSets/ClassifiedDataSetV1.1")

#Get Score
print("ScoreData:")
scoreList = myDataHandler.getScoreData()
print(f"\u001b[4m\u001b[1m{'Sentence  [0]':100} Score  [1]\u001b[0m")
for sentence in scoreList[:2]:
    #just some color output
    color = "\u001b[33;1m"
    if sentence[1] == "Positiv":
        color = "\u001b[32;1m"
    elif sentence[1] == "Negative":
        color = "\u001b[31;1m"

    print(f"{sentence[0]:100}|{color}{sentence[1]}\u001b[0m")

print("-"*111,"\n")


#Get Content Type
print("ContentTypeData:")
contentTypeList = myDataHandler.getContentTypeData()
print(f"\u001b[4m\u001b[1m{'Sentence  [0]':100} ContentType  [1]\u001b[0m")
for sentence in contentTypeList[7:9]:
    print(f"{sentence[0]:100}|{sentence[1]}\u001b[0m")

print("-"*118, "\n")


#Get Categorie
print("CategorieData:")
categorieList = myDataHandler.getCategorieData('Staff')
print(f"\u001b[4m\u001b[1m{'Sentence  [0]':100} Categorie  [1]\u001b[0m")
for sentence in categorieList[36:39]:
    print(f"{sentence[0]:100}|{sentence[1]}\u001b[0m")

print("-"*118, "\n")