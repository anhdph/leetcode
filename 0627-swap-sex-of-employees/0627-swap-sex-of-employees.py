import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].map({
        'f': 'm',
        'm': 'f'
    })

    return salary