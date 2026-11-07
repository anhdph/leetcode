import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    result = customers['name'][~customers['id'].isin(orders['customerId'])]

    return pd.DataFrame({'Customers': result})