import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    id = orders['customerId'].unique()

    result = customers['name'][~customers['id'].isin(id)]

    return pd.DataFrame({'Customers': result})