# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 2


from faker import Faker
from pathlib import Path
import numpy as np
import matplotlib as plt
import pandas as pd
import json
import pprint



fake = Faker()

#Create the data frame that contains the first and last names.
def fakeFrameMaker():

    fake = Faker()

    global fakerFrame
    fakeFirstNames = []
    fakeLastNames = []

    for _ in range(100):
        fakeFirstNames.append(fake.first_name())
        fakeLastNames.append(fake.last_name())

    nameDict = {"First names": fakeFirstNames, "Last names": fakeLastNames}

    jsonNameStuff = json.dumps(nameDict, indent=2)

    Path("names.json").touch()

    with open('names.json', 'w') as outfile:
        outfile.write(jsonNameStuff)

    #try:
    #    Path("charts").mkdir()
    #except FileExistsError:
    #    pass


    fakerFrame = pd.DataFrame(
        {
            "First Name": fakeFirstNames,
            "Last Name": fakeLastNames
        }
    )
fakeFrameMaker()

#print(fakerFrame)