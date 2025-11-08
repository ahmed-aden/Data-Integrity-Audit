import pandas as pd

# load dataset
df = pd.read_csv("property_data.csv", sep='\t')

# check for missing values
missing_summary = df.isnull().sum()

# detect duplicates
duplicates = df[df.duplicated()]
num_duplicates = len(duplicates)

# check for inconsistent values
# negative land
neg_land = df[df["Land_Area"] < 0]


# invalid dates
def validate_date(date_str):
    try:
        pd.to_datetime(date_str, errors='raise')
        return True
    except:
        return False
    
invalid_dates = df[~df["Sale_Date"].apply(validate_date)]

# summary report 
print(f"==== Data Summary Report ====")
print(f"Missing values: \n{missing_summary}\n")
print(f"Duplicate records: {num_duplicates}")
print(f"Negative land areas: {len(neg_land)}")
print(f"Invalid dates: {len(invalid_dates)}")

