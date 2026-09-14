import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(
        orders['customerId'].drop_duplicates(),
        left_on='id',
        right_on='customerId',
        how='left'
    )

    df.rename(columns={'name': 'Customers'}, inplace=True)

    return df.loc[df['customerId'].isna(), ['Customers']]