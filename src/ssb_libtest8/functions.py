"""A collection of useful functions.

The template and this example uses Google style docstrings as described at:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

import pandas as pd


def a_in_b(
    df_a: pd.DataFrame, df_b: pd.DataFrame, col_a: str, col_b: str = ""
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Finds overlap between two columns in two datasets, returns three dataframes, only in a, overlap and only in b.

    Args:
        df_a (pd.DataFrame): The left dataset
        df_b (pd.DataFrame): The right dataset
        col_a (str): The left column name
        col_b (str): The right column name (replaced by the value of col_a, if empty)

    Returns:
        pd.DataFrame: The data of A, where the values are not in the column in b.
        pd.DataFrame: The merged data of A and B, where there is a overlap in the columns.
        pd.DataFrame: The data of B, where the values are not in the column in a.

    Examples:
        only_a, overlap, only_b = a_in_b(df_a, df_b, "snr_nudb")
    """
    if not col_b:
        col_b = col_a
    only_a = df_a[~df_a[col_a].isin(df_b[col_b].unique())]
    only_b = df_b[~df_b[col_b].isin(df_a[col_a].unique())]
    overlap_a = df_a[df_a[col_a].isin(df_b[col_b].unique())]
    overlap_b = df_b[df_b[col_b].isin(df_a[col_a].unique())]
    merged_overlap = overlap_a.merge(
        overlap_b, left_on=col_a, right_on=col_b, how="left"
    )
    return only_a, merged_overlap, only_b
