import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if len(salary) < 2:
        result = None
    else:
        result = salary.iloc[1]

    return pd.DataFrame({'SecondHighestSalary': [result]})