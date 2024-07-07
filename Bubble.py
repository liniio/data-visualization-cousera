import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'Sales': [12000, 14000, 16000, 18000, 20000, 22000, 25000, 23000, 20000, 18000, 16000, 14000],
        'Seasonality': [0.5, 0.7, 0.9, 1.2, 1.5, 1.8, 2.0, 1.9, 1.5, 1.2, 0.9, 0.7]}  

df = pd.DataFrame(data)

# Normalize the seasonality values for bubble size
normalized_size = df['Seasonality'] * 100

# Create the bubble plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Sales'], s=normalized_size, alpha=0.7, cmap='viridis', edgecolors='w', linewidth=1)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.title('Impact of Seasonality on Automobile Sales')

# Adding a colorbar legend for bubble size
plt.colorbar(label='Seasonality Impact')

# Display the bubble plot
plt.grid(True)
plt.show()
