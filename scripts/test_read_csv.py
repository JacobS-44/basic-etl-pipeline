# test_read_csv.py
import pandas as pd

csv_path = '/Users/jakesearle/Projects/Data_Engineering_Projects/data/raw/users.csv'
print("Attempting to read CSV file from:", csv_path)

try:
    users_df = pd.read_csv(csv_path)
    print("CSV file read successfully!")
    print(users_df.head())  # Print the first few rows of the DataFrame
except Exception as e:
    print("Error occurred:", e)

def extract_users():
    users_df = pd.read_csv('../data/raw/users.csv')
    return users_df
