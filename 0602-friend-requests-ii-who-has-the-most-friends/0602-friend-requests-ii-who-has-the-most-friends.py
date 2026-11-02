import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    ids = pd.concat(
        [request_accepted['requester_id'],
        request_accepted['accepter_id']]
        )

    df = ids.value_counts().reset_index()
    df.columns = ['id', 'num']

    return df.head(1)