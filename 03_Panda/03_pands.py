import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Amit", "Sneha", "Rahul"],
    "Age": [23, 25, 23, 22, 25],
    "City": ["Delhi", "Mumbai", "Delhi", "Kolkata", "Mumbai"],
    "Marks": [85, 90, 85, 88, 92],
    "Gender": ["M", "M", "M", "F", "M"]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:\n", df)

# 1. value_counts()  -> Frequency of unique values
print("\nCity Value Counts:\n")
print(df["City"].value_counts())

# 2. drop_duplicates()  -> Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\nAfter Removing Duplicates:\n", df_no_duplicates)

# Remove duplicates based on specific column
df_unique_name = df.drop_duplicates(subset="Name")
print("\nUnique Names Only:\n", df_unique_name)

# 3. rename()  -> Rename column names
df = df.rename(columns={"Marks": "Score"})
print("\nAfter Renaming 'Marks' to 'Score':\n", df)

# 4. apply()  -> Apply custom function
# Add 5 bonus marks
df["Score"] = df["Score"].apply(lambda x: x + 5)

# Create new column based on condition
df["Pass"] = df["Score"].apply(lambda x: "Yes" if x >= 90 else "No")

print("\nAfter apply() operations:\n", df)

# 5. map()  -> Replace values using dictionary mapping
gender_map = {"M": "Male", "F": "Female"}
df["Gender"] = df["Gender"].map(gender_map)

print("\nAfter map() on Gender column:\n", df)

# 6. pivot_table()  -> Summarize data like Excel Pivot
# Average Score per City
pivot_city = df.pivot_table(
    values="Score",
    index="City",
    aggfunc="mean"
)

print("\nPivot Table (Average Score per City):\n", pivot_city)

# City vs Gender pivot
pivot_city_gender = df.pivot_table(
    values="Score",
    index="City",
    columns="Gender",
    aggfunc="mean"
)

print("\nPivot Table (City vs Gender):\n", pivot_city_gender)

# 7. Handling Categorical Data
# Convert City column to category type
df["City"] = df["City"].astype("category")

print("\nData Types After Converting City to Category:\n")
print(df.dtypes)

# Show category labels
print("\nCity Categories:\n", df["City"].cat.categories)

# Encode categories as numerical codes
df["City_Code"] = df["City"].cat.codes

print("\nAfter Encoding Categorical Data:\n", df)

# 8. dtype Conversion
# Convert Age to float
df["Age"] = df["Age"].astype("float")

print("\nAfter Converting Age to Float:\n")
print(df.dtypes)

# 9. BASIC EDA WORKFLOW

print("\n--- BASIC EDA WORKFLOW ---")

# 1. Structure Overview
print("\nFirst 5 Rows:\n", df.head())
print("\nShape of DataFrame:", df.shape)
print("\nDataFrame Info:\n")
print(df.info())

# 2. Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# 3. Statistical Summary (Numeric)
print("\nStatistical Summary (Numeric Columns):\n")
print(df.describe())

# 4. Statistical Summary (Categorical)
print("\nStatistical Summary (Categorical Columns):\n")
print(df.describe(include="object"))

# 5. Duplicate Check
print("\nNumber of Duplicate Rows:", df.duplicated().sum())

# 6. GroupBy Example (Average Score by City)
grouped = df.groupby("City")["Score"].mean()
print("\nGroupBy - Average Score by City:\n", grouped)