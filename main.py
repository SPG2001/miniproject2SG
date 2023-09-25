# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 2


from faker import Faker
from pathlib import Path
import numpy as np
import matplotlib as plt
import pandas as pd
import json


fake = Faker()

#Create the data frame that contains the first and last names.
def fakeNameMaker():

    fakeFirstNames = []
    fakeLastNames = []

    #generates a large number of names

    for _ in range(1000):
        fakeFirstNames.append(fake.first_name())
        fakeLastNames.append(fake.last_name())

    #Throw the names into a dictionary then a json file.

    nameDict = {"first names": fakeFirstNames, "last names": fakeLastNames}

    jsonNameStuff = json.dumps(nameDict, indent=2)

    Path("names.json").touch()

    with open('names.json', 'w') as outfile:
        outfile.write(jsonNameStuff)

#This takes the names out of the json file and throws them into a pandas frame.
def fakePandasMaker():

    global fakerFrame

    with open("names.json", 'r') as nameFile:

        fakeJsonNames = {}

        fakeJsonNames = json.load(nameFile)

        fakerFrame = pd.DataFrame.from_dict(fakeJsonNames, orient="columns")


#This makes the charts.
def fakeNameChart():

    #First, the charts directory is made.
    try:
        Path("charts").mkdir()
    except FileExistsError:
        pass

    #Count occurences of names in pandas dataframe.
    firstNameCount = fakerFrame.groupby('first names')['first names'].count()
    lastNameCount = fakerFrame.groupby('last names')['last names'].count()






fakeNameMaker()
fakePandasMaker()
fakeNameChart()