"""
Demo: Working with CSV Files using pandas
-----------------------------------------

This simple Python script shows how to:
1. Load a CSV file into pandas.
2. Explore the data.
3. Add a new record.
4. Save the updated data back to the same file.

Make sure you have pandas installed before running:
    pip install pandas
"""

import pandas as pd

# --------------------------------------------------------
# Step 1: Load the CSV file into a pandas DataFrame
# --------------------------------------------------------
# Replace this path with your actual file location if needed
csv_file = "SynthData.csv"

# Read the CSV file into a DataFrame (like a spreadsheet in memory)
data = pd.read_csv(csv_file)

# Display the first few rows to see what the data looks like
print("=== Original Data ===")
print(data.head())  # shows first 5 rows

# --------------------------------------------------------
# Step 2: Show some basic information about the dataset
# --------------------------------------------------------
print("\n=== Data Info ===")
print(data.info())  # column names, data types, non-null counts

print("\n=== Summary Statistics ===")
print(data.describe())  # quick summary for numeric columns

# --------------------------------------------------------
# Step 3: Add a new record (row) to the DataFrame
# --------------------------------------------------------
# Let's assume the CSV has columns like "Name", "Age", "Country"
# (Adjust this part based on your file’s actual columns)
new_record = {
    data.columns[0]: "New Entry",   # Replace with actual column names if known
    data.columns[1]: 99,
    data.columns[2]: "ExampleLand"
}

# Append the new row to the DataFrame
data = pd.concat([data, pd.DataFrame([new_record])], ignore_index=True)

print("\n=== Data After Adding New Record ===")
print(data.tail())  # show last few rows to confirm new record

# --------------------------------------------------------
# Step 4: Save the updated DataFrame back to the same CSV file
# --------------------------------------------------------
data.to_csv(csv_file, index=False)

print("\n✅ Data successfully saved back to 'SynthData.csv'")
