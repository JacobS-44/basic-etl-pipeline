import pandas as pd

#Step 1: Extract
def extract_sales():
    sales_df = pd.read_csv('../Data_Engineering_Projects/data/raw/sales.csv')
    return sales_df

def extract_users():
    users_df = pd.read_csv('../Data_Engineering_Projects/data/raw/users.csv')
    return users_df


#Step 2: Transform
def transform_data(users_df, sales_df):
    #Merge data on user_id
    merged_df = pd.merge(sales_df, users_df, on='user_id')
    #Calculate total sales per user
    total_sales = merged_df.groupby('name')['amount'].sum().reset_index()
    total_sales.columns = ['name', 'total_sales']
    return total_sales

#Step 3: Load
def load_data(transformed_df):
    transformed_df.to_csv('../Data_Engineering_Projects/data/processed/total_sales.csv', index=False)
    print("Data loaded successfully!")

#Main ETL Function
def main():
    users = extract_users()
    sales = extract_sales()
    transformed_data = transform_data(users, sales)
    load_data(transformed_data)

if __name__ == "__main__":
    main()