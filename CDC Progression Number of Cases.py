import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

covid = pd.read_csv('CDC Progression Number of Cases.csv', encoding='latin1')

covid = covid.dropna()

plt.figure(figsize=(8,5))
plt.title('CDC Progression Number of Cases')


print(covid['Total Cases'].tolist())

plt.plot(covid['Date'], covid['Total Cases'], label='Total Cases')
plt.plot(covid['Date'], covid['Rate per 100000'], label='Rate per 100000')

print(covid.Date[::15])

plt.xticks(covid.Date[::15])

plt.xlabel('Date (Month/Year)')
plt.ylabel('Total COVID-19 Cases')

plt.legend()

plt.show()
