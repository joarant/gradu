# asioita jota tarvitaan:
# Otsikko
# Teksti
# aiheet
# aika

# aiheet

# kotimaa "18-34837",
# urheilu "18-220090",
# sää  "18-215833",
# ulkomaat "18-34953",
# politiikka "18-220306",
# talous "18-204933",
# kulttuuri "18-208149",
# tiede "18-212923",
# luonto "18-215452",
# oppiminen "18-204676", # tiputa sillä liian epämääräinen aihe
# kolumnit "18-215844",



import json
import csv
import os
import pandas as pd
import xml.etree.ElementTree as ET


subjectsOfIntrest = [
"18-34837",
"18-220090",
"18-215833",
"18-34953",
"18-220306",
"18-204933",
"18-208149",
"18-212923",
"18-215452",
"18-204676",
"18-215844",
]

from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class Subjects(ExtendedEnum):
    kotimaa= "18-34837"
    urheilu= "18-220090"
    sää = "18-215833"
    ulkomaat ="18-34953"
    politiikka ="18-220306"
    talous= "18-204933"
    kulttuuri ="18-208149"
    tiede ="18-212923"
    luonto ="18-215452"
    oppiminen ="18-204676"
    kolumnit ="18-215844"



# def getAttributesFromJson(path):
#     f = open(path, encoding="utf8")
#     jsonFile = json.load(f)
#     tempObject = []
#     for article in jsonFile["data"]:
#         fullText = ""
#         for paragraph in article["content"]:
#             if paragraph["type"] == "text":
#                 fullText = fullText + "\n " + paragraph["text"]
#         articleObject = {"id" : article["id"], "url": article["url"]["short"], "headline": article["headline"]["full"], "text": fullText, "subjects": article.get("subjects", None), "datePublished": article["datePublished"]}
#         tempObject.append(articleObject)
        
#     f.close()
#     return tempObject

def getAttributesFromJson2(path):
    f = open(path, encoding="utf8")
    jsonFile = json.load(f)
    tempObject = []
    for article in jsonFile["data"]:
        finalSubjects = []
        subjects = article.get("subjects", None)
        if subjects is not None:
            for subject in subjects:
                if subject["id"] in Subjects.list():
                    finalSubjects.append(Subjects(subject["id"]).name)
                    # Subjects(subject["id"]).name
        if len(finalSubjects) > 0:
            fullText = ""
            for paragraph in article["content"]:
                if paragraph["type"] == "text":
                    fullText = fullText + "\n " + paragraph["text"]
            # articleObject = {"id" : article["id"], "url": article["url"], "headline": article["headline"]["full"], "text": fullText, "subjects": article.get("subjects", None), "datePublished": article["datePublished"]}
            articleObject = {"id" : article["id"], "url": article["url"], "headline": article["headline"]["full"], "text": fullText, "subjects": finalSubjects, "datePublished": article["datePublished"]}
            tempObject.append(articleObject)
        
    f.close()
    return tempObject


def list_files(startpath):
    paths = []
    for root, dirs, files in os.walk(startpath, topdown=False):
        for name in files:
            paths.append(os.path.join(root, name))
    return paths


# yksi alto on yksi sivu
# teksti on jäsennelty kappaleisiin
# sanat on eroteltu <sp> tageilla
# halutaan ainakin issn, lehden nimi, vuosi, teksti, lehden numero
def getTextFromXml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    xmlText = "" 
    for block in root.iter('TextBlock'):
        for node in block:
            for string in node:
                if string.tag == "SP":
                    xmlText = xmlText + " "
                if string.tag == "String":
                    xmlText = xmlText + string.get("CONTENT")

    xmlText = xmlText + "\n"
    print(xmlText)


    
def writeToFile(data, name):
    filename = name

    data.to_csv(filename, sep='␞', encoding='utf-8', index=False,)

getTextFromXml('../corpus/ocr sanomalehdet/klk_fi_1771_1874/arc01/0355-0257/1841/0355-0257_1841_1/alto/00001.xml')


documents = []
for file in list_files("../ylenews-fi-2011-2018-src/data/fi"):
    documents = documents + getAttributesFromJson2(file)
print(len(documents))
# print(documents[0]["id"])

df = pd.DataFrame(documents)
writeToFile(df, "2011-2018-3.csv")
print(len(df))
print(df.iloc[0]["id"])


# df = pd.read_csv('output.csv', sep='␞')

# print(len(df))
# print(df.columns)
# print(df.iloc[0]["id"])


# koko 2011-2018 457795 artikkelia