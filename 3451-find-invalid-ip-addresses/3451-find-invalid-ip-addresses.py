import pandas as pd

def is_invalid(ip: str) -> bool:
    octets = ip.split('.')

    if len(octets) != 4:
        return True
    
    for octet in octets:
        if len(octet) > 1 and octet.startswith('0'):
            return True
        
        if not octet.isdigit():
            return True

        if int(octet) > 255:
            return True

    return False

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    invalid = logs['ip'].apply(is_invalid)

    df = logs.loc[invalid, ['ip']]

    return (
        df.groupby('ip').agg(
            invalid_count=('ip', 'count')
        ).reset_index()
        .sort_values(['invalid_count', 'ip'], ascending=([False, False]))
    )