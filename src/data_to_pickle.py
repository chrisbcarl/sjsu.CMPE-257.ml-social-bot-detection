import os
import pickle
import warnings
import pandas as pd

def data_to_pickle(filepath, pickle_filepath):
    # type: (str, str) -> list[tuple[str, str]]
    changed_columns = []
    # if os.path.isfile(pickle_filepath) and os.path.getsize(filepath) / os.path.getsize(pickle_filepath) > 0.3:
    #     changed_columns += [('pickle', 'exists')]
    #     return changed_columns

    ext = os.path.splitext(filepath)[1]
    if ext.lower() == '.json':
        try:
            df = pd.read_json(filepath, encoding='utf-8', orient='records')
        except UnicodeDecodeError:
            df = pd.read_json(filepath, encoding='latin-1', orient='records')
    elif ext.lower() == '.csv':
        try:
            df = pd.read_csv(filepath, encoding='utf-8', low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(filepath, encoding='latin-1', low_memory=False)
    else:
        raise NotImplementedError(f'no parser implemented for {ext.lower()!r}')

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
