from pathlib import Path 
import pandas as pd
data_folder = Path(__file__).resolve().parent/"data"
csv_files = sorted(data_folder.glob("*.csv"))
print("Total CSV files;",len(csv_files))
for file in csv_files:
    df = pd.read_csv(file)

    
    print("\nFile:",file.name)
    print("Rows and Columns:",df.shape)
    print("Data Types:")
    print(df.dtypes)
    print("First 5 Rows:")
    print(df.head())
    print("Missing Values:",df.isnull().sum().sum())
    print("Duplicate Rows:",df.duplicated().sum())

fund_file = next(data_folder.glob("*01_fund_master.csv"))
fund_df = pd.read_csv(fund_file)

print("\nFund Master Columns:")
print(fund_df.columns.tolist())

print("\nFund Houses:")
print(fund_df["fund_house"].unique())

print("\nCategories:")
print(fund_df["category"].unique())

print("\Sub Categories:")
print(fund_df["sub_category"].unique())

print("\nRisk Categories:")
print(fund_df["risk_category"].unique())


nav_file = next(data_folder.glob("*02_nav_history.csv"))
nav_df = pd.read_csv(nav_file)

missing_codes = set(fund_df["amfi_code"]) - set(nav_df["amfi_code"])

print("\nAMFI Code Validation:")
print("Missing AMFI Codes:", missing_codes)

print("\nData Quality Summary:")
print("Total CSV files:", len(csv_files))
print("Fund Master records:", len(fund_df))
print("NAV History records:", len(nav_df))
print("Missing AMFI codes:", len(missing_codes))