import pandas as pd

## Adding columns
employeeData ={
    "Name":["Ram","Ram","Rohit","Rohit","Romit","Romit"],
    "Age":[20,22,45,34,25,33],
    "Salary":[30000,32000,100000,40000,35000,40000],
    "Performance Score":[85,90,99,40,96,90]
}
df_employee = pd.DataFrame(employeeData)
print(df_employee)

# Stright method
df_employee["Bonus"] = df_employee["Salary"] * 0.1
print(df_employee)

# Using insert method
df_employee.insert(0, "Employee ID", [10,20,30,40,50,60])
print(df_employee)

# Update data
df_employee.loc[0, "Salary"] = 50000
print(df_employee)

# increment the salary by 5 percent
df_employee["Salary"] = df_employee["Salary"] * 1.05
print(df_employee)

# Deleting a row and columns
# remove a singal coloumn
print("Modified data")
df_employee.drop(columns=["Performance Score"], inplace=False)
print(df_employee)

# for multiple columns
print("Modified data")
df_employee.drop(columns=["Performance Score","Age"], inplace=True)
print(df_employee)

# finding the missing values
employeesData ={
    "Name":["Ram", None, "Rahul","Rohit","Rohan","Romit","Rinku"],
    "Age":[20,None,22,45,34,25,33],
    "Salary":[30000,None,32000,100000,40000,35000,40000],
    "Performance Score":[85,None,90,99,40,96,90]
}
df_employees = pd.DataFrame(employeesData)
print(df_employees)
# missing values
print(df_employees.isnull())

# Total missing values
print(df_employees.isnull().sum())

# removing missing values
miss = df_employees.dropna(axis=0, inplace=False)
print(miss)

# set any defualt value on place of missing values
fill = df_employees.fillna(0, axis=0, inplace=False)
print(fill)

# fill the missing value with mean value
df_employees["Age"].fillna(df_employees["Age"].mean(), inplace=True)
df_employees["Salary"].fillna(df_employees["Salary"].mean(), inplace=True)
print(df_employees)

# # Sorting DataFrame by Salary column
sorted_salary = df_employee.sort_values(by="Salary", ascending=True, inplace=False)
print("\nSorted by Salary (Ascending):")
print(sorted_salary)

# Sorting multiple row
sorted_multiple = df_employee.sort_values(by=["Salary","Name"], ascending=[False,True], inplace=False)
print("\nSorted by Multiple (Ascending):")
print(sorted_multiple)

# Average and mean of a columns
avg_sal = df_employee["Salary"].mean()
print("Average mean of salary")
print(avg_sal)

sum_sal = df_employee["Salary"].sum()
print("Average sum of salary")
print(sum_sal)

# Using groupby using on singal column
grouped = df_employee.groupby("Name")["Salary"].sum()
print(grouped)

# Using groupby using on multiple column
data = {
    "Department": ["IT", "IT", "HR", "HR", "IT", "HR", "Finance", "Finance"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [60000, 65000, 40000, 42000, 62000, 43000, 70000, 72000],
    "Experience": [3, 4, 2, 3, 5, 4, 6, 7]
}

df_company = pd.DataFrame(data)
print(df_company)
grouped = df_company.groupby(["Department", "Gender"])["Salary"].mean()
print(grouped)

# Interpolation
# Interpolation = estimating missing values inside your dataset based on existing values.
# - Preserves Data Continuity
# - Better Than Mean Filling
# - Required Before ML Models
# - Improves Visualization

# Linear Interpolation (Default)
df_linear = pd.DataFrame({
    'value': [10, 20, None, 40, 50]
})
print(df_linear.interpolate(method='linear'))

# Time-Based Interpolation
df_time = pd.DataFrame({
    'value': [100, None, 300]
}, index=pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-04']))
print(df_time.interpolate(method='time'))

# Polynomial Interpolation
df_poly = pd.DataFrame({
    'value': [1, 4, None, 16, 25]
})
print(df_poly.interpolate(method='polynomial', order=2))

# Forward Fill (ffill)
df_forward = pd.DataFrame({
    'value': [10, None, None, 40]
})
print(df_forward.interpolate(method='pad'))

# Backward Fill (bfill)
print(df_forward.interpolate(method='backfill'))

# Merge 
df1 = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Ram", "Rahul", "Rohit", "Rohan"],
    "DeptID": [101, 102, 103, 104],
    "Department": ["IT", "HR", "Finance","Tech"]
})

df2 = pd.DataFrame({
    "DeptID": [101, 102, 105],
    "Department": ["IT", "HR", "Finance"]
})

# INNER MERGE (Default)
print(pd.merge(df1, df2, on="DeptID", how="inner"))

# LEFT MERGE
print(pd.merge(df1, df2, on="DeptID", how="left"))

# RIGHT MERGE
print(pd.merge(df1, df2, on="DeptID", how="right"))

# MERGE ON DIFFERENT COLUMN NAMES
print(pd.merge(df1, df2, left_on="DeptID", right_on="DeptID", how="inner"))

# MERGE ON MULTIPLE COLUMNS
print(pd.merge(df1, df2, on=["DeptID", "Department"], how="inner"))

# cross join
cross_join = pd.merge(df1, df2, how="cross")
print("\nCROSS JOIN RESULT:")
print(cross_join)

# Concatenation
df3 = pd.DataFrame({
    "Name": ["Ram", "Rahul"],
    "Age": [20, 22]
})

df4 = pd.DataFrame({
    "Name": ["Rohit", "Rohan"],
    "Age": [25, 30]
})

# Vertical Concatenation
result = pd.concat([df3, df4], ignore_index=True)
print(result)

# Horizontal Concatenation
df5 = pd.DataFrame({
    "Name": ["Ram", "Rahul"],
    "Age": [20, 22]
})

df6 = pd.DataFrame({
    "Name": ["Rohit"],
    "Salary": [50000]
})

result = pd.concat([df5, df6], ignore_index=True)

print(result)