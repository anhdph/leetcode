import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    # 1. Find policyholders with duplicated tiv_2015
    duplicated_tiv = insurance['tiv_2015'].duplicated(keep=False)

    # 2. Find policyholders with unique (lat, lon)
    unique_city = ~insurance.duplicated(
        subset=['lat', 'lon'],
        keep=False
    )

    # 3. Filter rows satisfying both conditions
    filtered = insurance[duplicated_tiv & unique_city]

    # 4. Sum tiv_2016 and round to 2 decimal places
    result = filtered['tiv_2016'].sum().round(2)

    return pd.DataFrame({
        'tiv_2016': [result]
    })