import pandas as pd

# Read data from CSV file into a datafram

# Why encoding latin1?
# Agar file me special characters hain (€, ñ, etc.) to utf-8 kabhi kabhi fail karta hai.
# Agar utf-8 work karta hai to usko hi use karo. Otherwise latin1 safe fallback hai.

# r lagane se Python backslash ko normal character treat karega.
# df = pd.read_csv(r"C:\Users\lenovo\Documents\Data Science learning\03_Panda\sales_data_sample.csv", encoding = "utf-8")
df = pd.read_csv(r"C:\Users\lenovo\Documents\Data Science learning\03_Panda\sales_data_sample.csv", encoding = "latin1")
print(df)

# Read ddta from xlsx file into a datafram
df_xlsx = pd.read_excel(r"C:\Users\lenovo\Documents\Data Science learning\03_Panda\SampleSuperstore.xlsx")
print(df_xlsx)

# Read data fram json file into a datafram
df_json = pd.read_json(r"C:\Users\lenovo\Documents\Data Science learning\03_Panda\sample_Data.json")
print(df_json)

## Save your own created data
data = {
    "Name":["Ram","Shyam","Rohit"],
    "Age":[10,20,40],
    "City":["Delhi","Mumbai","UP"]
}
df_data = pd.DataFrame(data)
print(df_data)
# df_data.to_csv("output.csv", index=False)
# df_data.to_excel("outpot.xlsx", index=False)
# df_data.to_json("output.json", orient="records")

## Exploring the data
# Why do be need to explore the data
# - Understand the data set
# - identify the problem
# - plan next step

# print starting and last rows
print("Display first 10 rows")
print(df_json.head(10))

print("Display last 10 rows")
print(df_json.tail(10))

## for summerise the data
print("Dataset Information:")
x = df_xlsx.info()
print(x)

print("Dataset Information:")
print(df_data.info())

## Discribe method
# A summary of discriptive statistics for numerical coloum in your datafram
employeeData ={
    "Name":["Ram","Rahul","Rohit","Rohan","Romit","Rinku"],
    "Age":[20,22,45,34,25,33],
    "Salary":[30000,32000,100000,40000,35000,40000],
    "Performance Score":[85,90,99,40,96,90]
}
df_employee = pd.DataFrame(employeeData)
print("Simple Data fram")
print(df_employee)
print("Discriptive statistics")
print(df_employee.describe())
print(f"Shape: {df_employee.shape}")
print(f"Column Name: {df_employee.columns}")

## Select singal column
print("Name (Singal column return series)")
name = df_employee["Name"]
print(name)

# select multiple columns
subset = df_employee[["Name", "Salary"]]
print("\nSubset with name and Salary")
print(subset)

# Singal condition
high_salary = df_employee[df_employee["Salary"]>50000]
print("Employee with salary with > 50000")
print(high_salary)

# Multiple condition
filtered = df_employee[(df_employee["Age"]>30) & (df_employee["Salary"]>35000)]
print(f"Employee list Age > 30 and Salary >35000")
print(filtered)

# Using or condition
filter_with_or = df_employee[(df_employee["Age"]>30) | (df_employee["Performance Score"]>90)]
print("Employee older than 30 OR Performance score grater than 90")
print(filter_with_or)
