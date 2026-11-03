import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee = employee.drop_duplicates(
        subset='salary'
    ).sort_values(
        by='salary', ascending=False
    ).reset_index(
        drop=True
    )

    # return employee

    if len(employee['salary']) < 2:
        return pd.DataFrame({
            'SecondHighestSalary':
            [None]
        })
    else:
        return pd.DataFrame({
            'SecondHighestSalary':
            [employee['salary'][1]]
        })