from dataSet import list_files, get_attributes_from_json, writeToFile
from xmlData import get_text_from_xml
import pandas as pd



print(get_text_from_xml('../corpus/ocr sanomalehdet/klk_fi_1771_1874/arc01/0355-0257/1841/0355-0257_1841_1/alto/00001.xml'))

# documents = []
# for file in list_files("../ylenews-fi-2011-2018-src/data/fi"):
#     documents = documents + get_attributes_from_json(file)
# print(len(documents))

# df = pd.DataFrame(documents)
# writeToFile(df, "2011-2018-SubjectsInPaper-1.csv")
# print(len(df))
# print(df.iloc[0]["id"])
