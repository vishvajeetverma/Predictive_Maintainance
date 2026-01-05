import pandas as pd

# Load the raw data file
file_path = "/home/kaifalam/vishvajeet_verma/modaxe_obd_logger/data/2025-10-17 12-55-25.csv"
df = pd.read_csv(file_path, sep=';', engine='python')

# Display the first few rows and columns for quick inspection
print("Columns in the file:")
print(df.columns)
print("\nFirst 5 rows:")
print(df.head())


