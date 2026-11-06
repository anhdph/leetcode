import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        employee[['id', 'salary']],
        left_on='managerId',
        right_on='id',
        how='inner'
    )

    df = df['name'][df['salary_x'] > df['salary_y']]

    return pd.DataFrame({'Employee': df})