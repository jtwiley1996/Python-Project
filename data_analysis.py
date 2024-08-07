import pandas as pd

# Load the CSV file
data = pd.read_csv('data.csv')

# Display the first few rows of the dataframe
print(data.head())

# Additional analysis (e.g., statistical summary)
print("\nStatistical Summary:")
print(data.describe())

# Display data types
print("\nData Types:")
print(data.dtypes)