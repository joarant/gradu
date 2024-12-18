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



# paperin luokat:

# urheilu "18-220090",
# talous "18-204933",
# politiikka "18-220306",
# kulttuuri "18-208149",
# luonto "18-215452",
# 18-218480 - Onnettomuudet
# 18-209306 - Terveys
# 18-217206 - Rikokset
# 18-91232 - Liikenne ja kuljetus
# 18-35286 - Koulutus ja kasvatus

import json
import csv
import os
import pandas as pd
import xml.etree.ElementTree as ET


from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class Subjects(ExtendedEnum):
    kotimaa = "18-34837"
    urheilu = "18-220090"
    sää = "18-215833"
    ulkomaat = "18-34953"
    politiikka ="18-220306"
    talous = "18-204933"
    kulttuuri ="18-208149"
    tiede = "18-212923"
    luonto = "18-215452"
    oppiminen ="18-204676"
    kolumnit ="18-215844"


class SubjectsInPaper(ExtendedEnum):
    urheilu ="18-220090"
    talous= "18-204933"
    politiikka ="18-220306"
    kulttuuri= "18-208149"
    luonto= "18-215452"
    Onnettomuudet = "18-218480"
    Terveys = "18-209306"
    Rikokset = "18-217206"
    Liikenne_ja_kuljetus = "18-91232"
    Koulutus_ja_kasvatus = "18-35286"


class SubjectsInPaperExtended(ExtendedEnum):
    urheilu ="18-220090"
    talous= "18-204933"
    politiikka ="18-220306"
    kulttuuri= "18-208149"
    luonto= "18-215452"
    Onnettomuudet = "18-218480"
    Terveys = "18-209306"
    Rikokset = "18-217206"
    Liikenne_ja_kuljetus = "18-91232"
    Koulutus_ja_kasvatus = "18-35286"
    kotimaa = "18-34837"
    sää = "18-215833"
    ulkomaat = "18-34953"
    tiede = "18-212923"
    oppiminen = "18-204676"
    kolumnit = "18-215844"


def get_attributes_from_json(path):
    with open(path, encoding="utf8") as file:
        json_file = json.load(file)

    result = []
    for article in json_file["data"]:
        subjects = article.get("subjects", [])
        valid_subjects = [
            SubjectsInPaper(subject["id"]).name
            for subject in subjects
            if subject["id"] in SubjectsInPaper.list()
        ]

        if valid_subjects:
            content_text = "\n".join(
                paragraph["text"]
                for paragraph in article["content"]
                if paragraph["type"] == "text"
            )
            article_data = {
                "id": article["id"],
                "url": article["url"],
                "headline": article["headline"]["full"],
                "text": content_text,
                "subjects": valid_subjects,
                "datePublished": article["datePublished"],
            }
            result.append(article_data)

    return result


def list_files(startpath):
    paths = []
    for root, dirs, files in os.walk(startpath, topdown=False):
        for name in files:
            paths.append(os.path.join(root, name))
    return paths



def writeToFile(data, name):
    filename = name
    data.to_csv(filename, sep='␞', encoding='utf-8', index=False,)