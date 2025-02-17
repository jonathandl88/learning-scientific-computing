import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Gene", "Charlie", "Rex"],
    "Age": [10, 15, 30, 45, 60],
    "City": ["Atlanta", "Mexico City", "Louisiana", "Atlanta", "Chicago"]
}

df = pd.DataFrame(data)

# Print first 3 rows
# print(df.head(3))

# Print data types
# print(df.dtypes)

# Filtering for people older than 30 and printing only their Name and City
filtered_df = df[df["Age"] > 30][["Name", "City"]]

# Adding a new column
df["Salary"] = [50000, 60000, 55000, 70000, 65000]

# Adding a new column based on existing column
df["Tax"] = df["Salary"]*0.10

# Grouping the dataframe by City and calculating the mean there
grouped = df.groupby("City")["Age"].mean()

# Sorting the dataframe by Age in descending order
df_sorted = df.sort_values(by="Age", ascending=False)

# Renaming some columns
df = df.rename(columns={"Age": "Years", "City": "Location"})





