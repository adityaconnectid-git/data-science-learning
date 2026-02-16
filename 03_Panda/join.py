import pandas as pd

# Join
df1 = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Ram", "Rahul", "Rohit", "Rohan"],
    "DeptID": [101, 102, 103, 104]
})

df2 = pd.DataFrame({
    "DeptID": [101, 102, 105],
    "Department": ["IT", "HR", "Finance"]
})

# Now JOIN (Different from Merge)
df1_index = df1.set_index("DeptID")
df2_index = df2.set_index("DeptID")

print("\nJOIN - INNER:")
print(df1_index.join(df2_index, how="inner"))

print("\nJOIN - LEFT:")
print(df1_index.join(df2_index, how="left"))

print("\nJOIN - RIGHT:")
print(df1_index.join(df2_index, how="right"))

print("\nJOIN - OUTER:")
print(df1_index.join(df2_index, how="outer"))