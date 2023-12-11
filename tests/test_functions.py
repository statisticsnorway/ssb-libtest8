import pandas as pd

from ssb_libtest8 import functions


def test_a_in_b():
    df_a = pd.DataFrame(
        {
            "col_a": [1, 2, 3],
        }
    )
    df_b = pd.DataFrame(
        {
            "col_b": [2, 3, 4],
        }
    )
    only_a, overlap, only_b = functions.a_in_b(df_a, df_b, "col_a", "col_b")
    assert isinstance(only_a, pd.DataFrame)
    assert isinstance(only_b, pd.DataFrame)
    assert isinstance(overlap, pd.DataFrame)
    assert len(only_a) == 1
    assert len(only_b) == 1
    assert len(overlap) == 2
