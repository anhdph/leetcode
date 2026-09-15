import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['num1'] = logs['num'].shift(-1)
    logs['num2'] = logs['num'].shift(-2)

    return pd.DataFrame(
        {'ConsecutiveNums': logs[(logs['num'] == logs['num1']) & (logs['num'] == logs['num2'])]['num'].drop_duplicates()}
    )