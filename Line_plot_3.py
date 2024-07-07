import pandas as pd
import matplotlib.pyplot as plt

# Mở rộng DataFrame với nhiều dòng xe và nhiều năm
data = {'Year': [2018, 2018, 2018, 2019, 2019, 2019, 2020, 2020, 2020, 2021, 2021, 2021],
        'VehicleType': ['Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck'],
        'Sales': [12000, 10000, 8000, 14000, 12000, 10000, 10000, 9000, 8000, 11000, 9500, 7500],
        'UnemploymentRate': [4.0, 4.2, 4.5, 3.8, 4.0, 4.3, 8.5, 8.8, 9.0, 9.2, 9.5, 9.8]}

df = pd.DataFrame(data)

# Filter DataFrame for recession periods
recession_years = [2020, 2021]
recession_df = df[df['Year'].isin(recession_years)]

# Create a line plot for each vehicle type
plt.figure(figsize=(12, 8))

for vehicle_type in df['VehicleType'].unique():
    vehicle_type_df = recession_df[recession_df['VehicleType'] == vehicle_type]
    plt.plot(vehicle_type_df['Year'], vehicle_type_df['Sales'], marker='o', label=vehicle_type)

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales During Recession')

# Display the line plot
plt.legend()
plt.grid(True)
plt.show()
