import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {'Year': [2018, 2019, 2020, 2021],
        'GDP': [5000, 5500, 4800, 5200],
        'Recession': [0, 0, 1, 1]}  # 0: Non-recession, 1: Recession

df = pd.DataFrame(data)

# Create subplots for recession and non-recession periods
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

# Filter DataFrame for recession and non-recession periods
recession_df = df[df['Recession'] == 1]
non_recession_df = df[df['Recession'] == 0]

# Plot line chart for recession period
axes[0].plot(recession_df['Year'], recession_df['GDP'], marker='o', linestyle='-', color='r')
axes[0].set_ylabel('GDP')
axes[0].set_title('GDP Variation During Recession Period')

# Plot line chart for non-recession period
axes[1].plot(non_recession_df['Year'], non_recession_df['GDP'], marker='o', linestyle='-', color='b')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('GDP')
axes[1].set_title('GDP Variation During Non-Recession Period')

# Display the subplots
plt.tight_layout()
plt.show()
