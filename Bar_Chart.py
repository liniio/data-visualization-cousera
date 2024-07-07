import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Year': [2018, 2019, 2020, 2021, 2018, 2019, 2020, 2021],
        'VehicleType': ['Sedan', 'Sedan', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'SUV'],
        'Sales': [15000, 18000, 12000, 20000, 10000, 12000, 8000, 15000]}

df = pd.DataFrame(data)

# Assuming the recession period is from 2020 to 2021, and non-recession is before 2020
recession_years = [2020, 2021]
non_recession_years = [2018, 2019]

# Filter DataFrame for recession and non-recession periods
recession_df = df[df['Year'].isin(recession_years)]
non_recession_df = df[df['Year'].isin(non_recession_years)]

# Combine the DataFrames
combined_df = pd.concat([recession_df, non_recession_df])

# Plot using Seaborn bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=combined_df, x='Year', y='Sales', hue='VehicleType')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Trend Comparison per Vehicle Type (Recession vs. Non-Recession)')

# Display the chart
plt.legend(title='Vehicle Type')
plt.grid(True)
plt.show()
