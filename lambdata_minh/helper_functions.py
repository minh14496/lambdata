import pandas as pd
import numpy as np

def null_count(df):
    """
    Check a dataframe for nulls and return the number of missing values.

    Args:
        df ([type]): pandas dataframe
    Example Input (df = pd.DataFrame):
    > | column 0    | column 1    | column 2    |
    > | ----------- | ----------- | ----------- |
    > | NaN         | 9           | 10          |
    > | 4           | NaN         | 2           |
    > | 3           | NaN         | 2           |

    Function:
    > `null_count(df)`

    Expected Output (int):
    > `3`

    """
    return df.isna().sum().sum()

def train_test_split(df, frac):
    """
    Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 

    Args:
        df ([type]): pandas dataframe
        frac ([type]): referes to the precent of data you would like to set aside for training.

    Example Input (df = pd.DataFrame):
    > | column 0    | column 1    | column 2    |
    > | ----------- | ----------- | ----------- |
    > | 0           | 1           | 2           |
    > | 3           | 4           | 5           |
    > | 6           | 7           | 8           |

    Function:
    > `train_test_split(df, frac=0.2)`

    Expected Output (tuple of two dataframes):
        (
    > | column 0    | column 1    | column 2    | 
    > | ----------- | ----------- | ----------- |
    > | 3           | 4           | 5           |
        ,
    > | column 0    | column 1    | column 2    | 
    > | ----------- | ----------- | ----------- | 
    > | 0           | 1           | 2           |
    > | 6           | 7           | 8           |
        )

    """
    #type(frac)==float
        
    length = int(len(df)*frac)
    df1 = df[:length].copy()
    df2 = df[length:].copy()
    return df1, df2

def randomize(df, seed):
    """
    Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
    
    Args:
        df ([type]): pandas dataframe
        seed ([type]): an int input. Random seed for reproducible randomization

    Example Input (df = pd.DataFrame):
    > | column 0    | column 1    | column 2    |
    > | ----------- | ----------- | ----------- |
    > | 0           | 1           | 2           |
    > | 3           | 4           | 5           |
    > | 6           | 7           | 8           |

    Function:
    > `randomize(df, seed=101)`

    Expected Output (pd.Dataframe): 
    > | column 0    | column 1    | column 2    |
    > | ----------- | ----------- | ----------- |
    > | 2           | 5           | 8           |
    > | 0           | 3           | 6           |
    > | 1           | 4           | 7           |

    """
    df = df.sample(frac=1,random_state=seed)
    return df

# def addy_split(addy_series):
#     """
#     Split addresses into three columns (df['city'], df['state'], and df['zip']).
    
#     Args:
#         addy_series ([type]): pandas Series

#     Example Input (addy_series = pd.Series):
#     > | address                                    |
#     > | ------------------------------------------ |
#     > | 890 Jennifer Brooks\nNorth Janet, WY 24785 |
#     > | 8394 Kim Meadow\nDarrenville, AK 27389     |
#     > | 379 Cain Plaza\nJosephburgh, WY 06332      |
#     > | 5303 Tina Hill\nAudreychester, VA 97036    |

#     Function:
#     > `addy_split(addy_series)`

#     Expected Output (pd.Dataframe): 
#     > | city          | state       | zip         |
#     > | ------------- | ----------- | ----------- |
#     > | North Janet   | WY          | 24785       |
#     > | Darrenville   | AK          | 27389       |
#     > | Josephburgh   | WY          | 06332       |
#     > | Audreychester | VA          | 97036       |

#     """
#     return addy_series

    