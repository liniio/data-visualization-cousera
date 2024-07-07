import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Period': ['Recession', 'Recession', 'Non-Recession', 'Non-Recession'],
        'Expenditure': [200000, 180000, 250000, 280000],
        'Recession': [1, 1, 0, 0]}  # 1: Recession, 0: Non-recession

df = pd.DataFrame(data)

# Group by Period and sum the expenditures
expenditure_by_period = df.groupby('Period')['Expenditure'].sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(expenditure_by_period, labels=expenditure_by_period.index, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])

# Adding a title
plt.title('Advertising Expenditure of XYZAutomotives During Recession and Non-Recession Periods')

# Display the pie chart
plt.show()
