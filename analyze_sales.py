import pandas as pd

# 1. Define the file path
file_path = 'MultipleFiles/9. Sales-Data-Analysis.csv'

# 2. Load the CSV into a DataFrame
try:
    df = pd.read_csv(file_path)
    print(f"Successfully loaded data from: {file_path}")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the path and file name.")
    exit() # Exit the script if the file isn't found

# 3. Display the first few rows
print("\n--- First 5 rows of the DataFrame ---")
print(df.head())

# 4. Get basic information about the data (columns, non-null counts, data types)
print("\n--- DataFrame Info ---")
df.info()

# 5. Get descriptive statistics for numerical columns
print("\n--- Descriptive Statistics ---")
print(df.describe())

# 6. Check for missing values in each column
print("\n--- Missing Values per Column ---")
print(df.isnull().sum())

# 7. Check for duplicate rows
print("\n--- Number of Duplicate Rows ---")
print(df.duplicated().sum())

