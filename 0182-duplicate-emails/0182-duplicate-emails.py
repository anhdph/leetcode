import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup = person[person['email'].duplicated()]['email'].drop_duplicates()

    return pd.DataFrame({'Email': dup})