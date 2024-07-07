import pandas as pd
import matplotlib.pyplot as plt

# Mở rộng DataFrame với nhiều dòng xe và nhiều năm
data = {'Year': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021],
        'Sales': [12000, 14000, 10000, 11000, 9500, 7500, 16000, 18000, 12000, 20000, 22000, 25000],
        'AveragePrice': [25000, 24000, 26000, 27000, 28000, 26000, 30000, 28000, 32000, 35000, 33000, 31000],
        'Recession': [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]}  # 0: Non-recession, 1: Recession

df = pd.DataFrame(data)

# Filter DataFrame for recession periods
recession_df = df[df['Recession'] == 1]

# Scatter plot to identify correlation
plt.figure(figsize=(12, 8))

# Separate the data by Year for better visibility
for year in df['Year'].unique():
        year_df = recession_df[recession_df['Year'] == year]
        plt.scatter(year_df['Sales'], year_df['AveragePrice'], label=f'Year {year}', alpha=0.7, edgecolors='w', linewidth=1, s=150)

# Adding labels and title
plt.xlabel('Sales Volume')
plt.ylabel('Average Vehicle Price')
plt.title('Correlation between Average Vehicle Price and Sales Volume during Recessions')

# Display the scatter plot
plt.legend()
plt.grid(True)
plt.show()
