import pandas as pd
import matplotlib.pyplot as plt

# Install openpyxl if not already installed
# pip install openpyxl

# Load data from Excel
data = pd.read_excel('C:/Users/HP/Downloads/Social_distancing.xlsx')

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(data['Days'], data['People'], label='Affected People (Bar Chart)')
plt.title('Number of Affected People Over Time (Bar Chart)')
plt.xlabel('Days')
plt.ylabel('Number of Affected People')
plt.legend()
plt.grid(True)
plt.show()
