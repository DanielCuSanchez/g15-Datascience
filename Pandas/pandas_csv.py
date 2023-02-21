import pandas as pd

file = pd.read_csv("hurricanes.csv")
print(file.head())
print(file.columns)