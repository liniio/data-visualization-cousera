import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'VehicleType': ['Sedan', 'SUV', 'Truck', 'Sedan', 'SUV', 'Truck'],
        'Expenditure': [50000, 70000, 80000, 45000, 60000, 75000],
        'Recession': [1, 1, 1, 1, 1, 1]}  # 1: Recession

df = pd.DataFrame(data)

# Filter DataFrame for recession period
recession_df = df[df['Recession'] == 1]

# Group by VehicleType and sum the expenditures
expenditure_by_vehicle_type = recession_df.groupby('VehicleType')['Expenditure'].sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(expenditure_by_vehicle_type, labels=expenditure_by_vehicle_type.index, autopct='%1.1f%%', startangle=90)

# Adding a title
plt.title('Total Advertisement Expenditure by Vehicle Type During Recession')

# Display the pie chart
plt.show()
