import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = (
        employee.drop_duplicates(subset='salary')
        .sort_values(by='salary', ascending=False)
    )

    if len(employee) < N or N <= 0:
        return pd.DataFrame(
            {f'getNthHighestSalary({N})': [None]}
        )
    else:
        return pd.DataFrame(
            {f'getNthHighestSalary({N})': [employee['salary'].iloc[N-1]]}
        )