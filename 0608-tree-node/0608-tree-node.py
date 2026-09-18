import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:

    tree['type'] = None
    
    for row in tree.itertuples():

        if pd.isna(row.p_id):
            tree.loc[row.Index, "type"] = "Root"

        elif row.id not in tree["p_id"].dropna().unique():
            tree.loc[row.Index, "type"] = "Leaf"

        else: tree.loc[row.Index, "type"] = "Inner"

    return tree[['id', 'type']]
