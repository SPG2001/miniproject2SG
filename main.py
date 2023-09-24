from faker import Faker
import numpy as np
import matplotlib as plt
import pandas as pd

fakeData = []
fake = Faker()


def fakeFrameMaker():
    fakerFrame = pd.DataFrame(
        {
            "Name": [

            ],
            "Age": [],
            "Sex": []
        }
    )

    fakeData = []

    fakeName = Faker()
    fakeAge = Faker()
    fakeSex = Faker()

    #for _ in range(100):




print(fakeData)

fakerFrame = pd.DataFrame(
    {
        "Name": ["Stephen"

                 ],
        "Age": ["22"],
        "Sex": ["Male"]
    }
)

print(fakerFrame)