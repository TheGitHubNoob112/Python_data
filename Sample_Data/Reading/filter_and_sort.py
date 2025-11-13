import csv

# Read CSV file into a list of dictionaries
data = []
with open("Sample_Data/SynthData.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert Age and Salary to integers for sorting/filtering
        row["Age"] = int(row["Age"])
        row["Salary"] = int(row["Salary"])
        data.append(row)

# Sort the data by Age (ascending)
sorted_by_age = sorted(data, key=lambda x: x["Age"])

# Filter the data: e.g., people in 'Engineering' with Salary > 75000
filtered_data = [row for row in data if row["Department"] == "Engineering" and row["Salary"] > 75000]

# Print sorted data (first 5 rows)
print("Sorted by Age:")
for row in sorted_by_age[:5]:
    print(row)

# Print filtered data
print("\nFiltered (Engineering & Salary > 75000):")
for row in filtered_data [:5]:
    print(row)
