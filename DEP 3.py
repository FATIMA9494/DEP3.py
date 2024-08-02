python -m venv env
pip install pandas matplotlib openpyxl
import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file
data = pd.read_csv('input_data.csv')

# Perform some data analysis (e.g., basic statistics)
summary = data.describe()

# Visualize the data (e.g., a simple plot)
data['column_of_interest'].plot(kind='bar')
plt.title('Sample Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Save the summary statistics to a new CSV file
summary.to_csv('summary_statistics.csv', index=False)

print("Data analysis complete. Results saved to 'summary_statistics.csv'.")
