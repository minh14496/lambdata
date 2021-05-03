import pandas as pd
import numpy as np

df = pd.DataFrame()

def null_count(df):
    """
    Check a dataframe for nulls and return the number of missing values.

    Args:
        df ([type]): pandas dataframe
    """
    return df.isna().sum().sum()

def train_test_split(df, frac):
    """
    Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 

    Args:
        df ([type]): pandas dataframe
        frac ([type]): referes to the precent of data you would like to set aside for training.
    """
    assert type(frac)==float
    length = len(df)*frac
    df1 = df[:length].copy()
    df2 = df[length:].copy()
    return (df1,df2)
def randomize(df, seed):
    """
    Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
    
    Args:
        df ([type]): pandas dataframe
        seed ([type]): an int input. Random seed for reproducible randomization
    """
    df = df.sample(frac=1,random_state=seed)
    return df