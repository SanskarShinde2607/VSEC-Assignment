
import pandas as pd

df = pd.read_csv(
    "C:/Users/ADMIN/Desktop/python abhijit/PYTHON ASSIGNMENT/student_dataset_25.csv"
)

print("=" * 100)
print(df)
print("=" * 100)

# 1. FILTERING
print("1. FILTERING")

high_paid_employee = df[
    (df["Department"] == "IT") & (df["Salary"] > 25000)
]
print("## For IT Department\n", high_paid_employee)
print("=" * 100)

high_paid_employee = df[
    (df["Department"] == "Computer") & (df["Salary"] > 25000)
]
print("## For Computer Department\n", high_paid_employee)
print("=" * 100)

high_paid_employee = df[
    (df["Department"] == "Electronics") & (df["Salary"] > 25000)
]
print("## For Electronics Department\n", high_paid_employee)
print("=" * 100)

# 2. SORTING
df = df.sort_values(
    ["Age", "Salary"],
    ascending=[True, False]
)

print("2. SORTING")
print(df)
print("=" * 100)

# 3. GROUPING AND CALCULATING MEAN SALARY
df_grouped = df.groupby("Department")["Salary"].mean()

print("3. CALCULATING AVERAGE SALARY BY DEPARTMENT")
print(df_grouped)
print("=" * 100)
