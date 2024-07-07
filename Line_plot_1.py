import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Year': [2018, 2019, 2020, 2021],
        'Sales': [15000, 18000, 12000, 20000]}

df = pd.DataFrame(data)

# Plotting the Line Chart
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Sales'], marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.title('Automobile Sales Fluctuation Over Years')

# Display the line chart
plt.grid(True)
plt.show()