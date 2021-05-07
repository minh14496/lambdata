import pytest
import pandas as pd
import numpy as np
from helper import HelperDataFrame as hdf


# Create a random DataFrame
df = pd.DataFrame(np.random.random((5,3)))
# randomly choose what number below 0.5 to mask as Null
mask = np.random.random(df.shape) < 0.5
df = df.mask(mask)
hdf_test = hdf(df)
hdf_test_2 = hdf(pd.DataFrame())


def test_null_count():
    """
    test_null_count test null_count function in HelperDataFrame
    """
    assert hdf_test.null_count() == mask.sum()


def test_null_count_empty_df():
    """
    test_null_count with empty DataFrame
    """
    assert hdf_test_2.null_count() == 0


def test_train_test_split():
    h1, h2 = hdf_test.train_test_split()
    assert len(h1) + len(h2) == len(hdf_test.df)


def test_train_test_split_with_empty():
    h1, h2 = hdf_test_2.train_test_split()
    assert len(h1) + len(h2) == 0