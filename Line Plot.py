import pandas as pd
import matplotlib.pyplot as plt

# Install openpyxl if not already installed
# pip install openpyxl

# Load data from Excel
data = pd.read_excel('C:/Users/HP/Downloads/Social_distancing.xlsx')

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(data['Days'], data['People'], label='Affected People (Line Plot)', marker='o')
plt.title('Number of Affected People Over Time (Line Plot)')
plt.xlabel('Days')
plt.ylabel('Number of Affected People')
plt.legend()
plt.grid(True)
plt.show()



