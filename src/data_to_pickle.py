import os
import pickle
import warnings
import pandas as pd

def data_to_pickle(filepath, pickle_filepath):
    ext = os.path.splitext(filepath)[1]
    if ext.lower() == '.json':
        df = pd.read_json(filepath, dtype=str, orient='records')
    elif ext.lower() == '.csv':
        df = pd.read_csv(filepath, dtype=str, low_memory=False)
    else:
        raise NotImplementedError(f'no parser implemented for {ext.lower()!r}')

    changed_columns = []
    for col in df.select_dtypes(include=['object'], exclude=['str']).columns:
        df[col] = df[col].astype('category')
        changed_columns.append((col, 'category'))

    for col in df.columns:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                df[col] = pd.to_datetime(df[col])
                changed_columns.append((col, 'datetime'))
        except Exception:
            pass
        if df[col].nunique() < 100:
            df[col] = df[col].astype('category')
            changed_columns.append((col, 'category'))

    with open(pickle_filepath, 'wb') as f:
        pickle.dump(df, f)

    return changed_columns
