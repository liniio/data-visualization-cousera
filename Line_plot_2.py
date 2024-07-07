import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Year': [2018, 2019, 2020, 2021, 2018, 2019, 2020, 2021],
        'VehicleType': ['Sedan', 'Sedan', 'Sedan', 'Sedan', 'SUV', 'SUV', 'SUV', 'SUV'],
        'Sales': [15000, 18000, 12000, 20000, 10000, 12000, 8000, 15000]}

df = pd.DataFrame(data)

# Plotting lines for each vehicle type
plt.figure(figsize=(10, 6))

# Iterate over unique vehicle types and plot lines
for vehicle_type in df['VehicleType'].unique():
    subset_df = df[df['VehicleType'] == vehicle_type]
    plt.plot(subset_df['Year'], subset_df['Sales'], label=vehicle_type, marker='o', linestyle='-')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Trends for Different Vehicle Types')

# Adding a legend
plt.legend()

# Display the line chart
plt.grid(True)
plt.show()