# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 2


from faker import Faker
import numpy as np
import matplotlib as plt
import pandas as pd

fake = Faker()

#Create the data frame that contains the first and last names.
def fakeFrameMaker():

    fake = Faker()

    global fakerFrame
    fakeFirstNames = []
    fakeLastNames = []

    for _ in range(100):
        fakeFirstNames.append(fake.name())
        fakeLastNames.append(fake.name())

    fakerFrame = pd.DataFrame(
        {
            "First Name": fakeFirstNames,
            "Last Name": fakeLastNames
        }
    )
fakeFrameMaker()

print(fakerFrame)