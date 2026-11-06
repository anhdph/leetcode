import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        employee[['id', 'salary']],
        left_on='managerId',
        right_on='id',
        how='left'
    )

    df = df[df['salary_x'] > df['salary_y']]['name']

    return pd.DataFrame({'Employee': df})