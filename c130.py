import pandas as pd
import csv
data=pd.read_csv("total_stars.csv")
print(data.columns)
del data["Unnamed: 0"]
del data["Unnamed: 6"]
del data["Star_name.1"]
del data["Distance.1"]
del data["Mass.1"]
del data["Radius.1"]

data1=data.dropna()
data1.to_csv("final_data.csv")