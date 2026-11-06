import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['num_2'] = logs['num'].shift(1)
    logs['num_3'] = logs['num'].shift(2)

    result = logs['num'][
        (logs['num'] == logs['num_2']) &
        (logs['num_2'] == logs['num_3'])
    ].drop_duplicates()

    return pd.DataFrame({'ConsecutiveNums': result})