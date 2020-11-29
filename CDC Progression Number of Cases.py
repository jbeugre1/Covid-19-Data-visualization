import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

covid = pd_read.csv('CDC Progression Number of Cases.csv')

plt.figure(figsize=(8,5))
plt.title('CDC Progression Number of Cases')

plt.plot(covid['Date'], covid['Total Cases'], label='Total Cases', 'b.-')
plt.plot(covid['Date'], covid['Rate per 100000'], label='Rate per 100000', 'r.-')

print(covid.Date[::15])

plt.xticks(covid.Date[::15])

plt.xlabel('Date (Month/Year)')
plt.ylabel('Total COVID-19 Cases')

plt.legend()

plt.show()
