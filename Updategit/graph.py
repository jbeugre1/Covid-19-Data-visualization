import numpy as np
import pandas 

data = pandas.read_csv("us.csv")
column_name = []
for col in data.columns:
    column_name.append(str(col))

print(column_name[0])



