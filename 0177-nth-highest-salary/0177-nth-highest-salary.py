import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].sort_values(ascending=False).drop_duplicates()

    if (len(salary) >= N) & (N > 0):
        result = salary.iloc[N-1]
    else:
        result = None

    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})