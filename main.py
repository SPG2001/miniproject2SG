# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 2

# This project generates 1000 names from the faker package and sorts them by number of occurrences.

from faker import Faker
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import json


fake = Faker()

# This creates the data frame that contains the first and last names.
def fakeNameMaker():

    fakeFirstNames = []
    fakeLastNames = []

    #generates a large number of names

    for i in range(1000):
        fakeFirstNames.append(fake.first_name())
        fakeLastNames.append(fake.last_name())

    """Throw the names into a dictionary then a json file (This is to show that I am extracting from a json file 
       in order to correctly follow the assignment)"""

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

    # Count occurrences of names in pandas dataframe and sort them by the number occurrences.

    firstNameCount = fakerFrame.groupby('first names')['first names'].count().sort_values(ascending=[1]).tail()
    lastNameCount = fakerFrame.groupby('last names')['last names'].count().sort_values(ascending=[1]).tail()

    # This constructs the pair of graphs and saves them to the charts directory.

    firstNameCount.plot(x="Name", y="Occurrences", kind="bar")
    plt.xlabel('Names')
    plt.ylabel('Occurrences')
    plt.axis([-1, 5, 1, 40])

    savefile = "charts/firstnamecharts.png"
    plt.savefig(savefile)

    plt.show()

    lastNameCount.plot(x="Name", y="Occurrences", kind="bar")
    plt.xlabel('Names')
    plt.ylabel('Occurrences')
    plt.axis([-1, 5, 1, 40])

    savefile = "charts/lastnamecharts.png"
    plt.savefig(savefile)

    plt.show()


fakeNameMaker()
fakePandasMaker()
fakeNameChart()
