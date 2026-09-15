import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    banned_users = users['users_id'][
        (users['banned'] == 'Yes') &
        (users['role'].isin(['driver', 'client']))
    ]

    trips['request_at'] = pd.to_datetime(trips['request_at'])

    trips = trips[
        (trips['request_at'].between('2013-10-01', '2013-10-03')) &
        (~trips['client_id'].isin(banned_users)) &
        (~trips['driver_id'].isin(banned_users))
    ]
    
    cancelled = (
        trips.groupby('request_at')
        .agg(
            total = ('status', 'size'),
            cancelled = ('status', lambda x: (x != 'completed').sum())
        ).reset_index()
    )

    cancelled['rate'] = (
        cancelled['cancelled'] / cancelled['total']
    ).round(2)

    return cancelled[['request_at', 'rate']].rename(
        columns={'request_at': 'Day',
        'rate': 'Cancellation Rate'}
    )