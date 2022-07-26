import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('medals.csv')
# print(data.columns)

# YEAR
# print(data['Year'].unique())
bins = [0, 1914, 1918, 1939, 1945, 2022]
labels = ['before WW I','WW I','after WW I before WW II', 'WW II', 'after WW II']
data['Epoque'] = pd.cut(data['Year'], bins, labels =labels)
# print(data)
# City
# print(data['City'].unique())
# Sport
print(data['Sport'].unique())
# Discipline
print(data['Discipline'].unique())
# Athlete

# Country
print(data['Country'].unique())
# Gender
print(data['Gender'].unique())
# Event
print(data['Event'].unique())
# Medal
print(data['Medal'].unique())