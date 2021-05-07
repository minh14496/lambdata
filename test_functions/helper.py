import pandas as pd
import numpy as np
import math


class HelperDataFrame():
    def __init__(self, df=None, frac=0, seed=1):
        self.df = df
        self.frac = frac
        self.seed = seed

    def null_count(self):
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
        return self.df.isna().sum().sum()

    def train_test_split(self):

        """
        Create a Train/Test split function for a dataframe and
        returns both the Training and Testing sets.

        Args:
            df ([type]): pandas dataframe
            frac ([type]): referes to the precent of data you would like to set
            aside for training.

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
        # type(frac)==float
        length = math.ceil(len(self.df)*self.frac)
        df1 = self.df.iloc[:length].copy()
        df2 = self.df.iloc[length:].copy()
        return df1, df2

    def randomize(self):
        """
        Develop a randomization function that randomizes all of a dataframes cells 
        then returns that randomized dataframe. 
        
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
        self.df = self.df.sample(frac=1, random_state=self.seed)
        return self.df

    def rm_outlier(self):
        """
        rm_outlier A 1.5*Interquartile range outlier detection/removal function that 
        gets rid of outlying rows and returns that outlier cleaned dataframe.

        Example Input (df = pd.DataFrame):
        > | column 0    | column 1    | column 2    |
        > | ----------- | ----------- | ----------- |
        > | 0           | 1           | 2           |
        > | 3           | 850         | 5           |
        > | 6           | 7           | 8           |

        Function:
        > `rm_outlier(df)`

        Example Output (df = pd.DataFrame):
        > | column 0    | column 1    | column 2    |
        > | ----------- | ----------- | ----------- |
        > | 0           | 1           | 2           |
        > | 6           | 7           | 8           |
        """
        for col in self.df.columns:
            limit = np.percentile(self.df[col],50) * 1.5
            self.df.drop(self.df[self.df[col] > limit].index, inplace=True)
        return self.df


class HelperSeries(HelperDataFrame):
    def __init__(self, df=None, frac=0, seed=1, series=None, abbr_2_st=True):
        super().__init__(self, df=None, frac=0, seed=1)
        self.series = series
        self.abbr_2_st = abbr_2_st
        
    def addy_split(self):
        """
        Split addresses into three columns (df['city'], df['state'], and df['zip']).

        Example Input (addy_series = pd.Series):
        > | address                                    |
        > | ------------------------------------------ |
        > | 890 Jennifer Brooks\nNorth Janet, WY 24785 |
        > | 8394 Kim Meadow\nDarrenville, AK 27389     |
        > | 379 Cain Plaza\nJosephburgh, WY 06332      |
        > | 5303 Tina Hill\nAudreychester, VA 97036    |

        Function:
        > `addy_split(addy_series)`

        Expected Output (pd.Dataframe): 
        > | city          | state       | zip         |
        > | ------------- | ----------- | ----------- |
        > | North Janet   | WY          | 24785       |
        > | Darrenville   | AK          | 27389       |
        > | Josephburgh   | WY          | 06332       |
        > | Audreychester | VA          | 97036       |

        """
        df = pd.DataFrame(self.series)
        df['city'] = df['address'].apply(lambda x: x.split('\n')[-1].split(',')[0])
        df['state'] = df['address'].apply(lambda x: x.split('\n')[-1].split(',')[-1].
        strip().split(' ')[-2])
        df['zip'] = df['address'].apply(lambda x: x.split('\n')[-1].split(',')[-1].
        strip().split(' ')[-1])
        df = df.drop(columns='address')
        return df
    
    def abbr_2_st(self):
        """
        abbr_2_st Return a new column with the full name from a State abbreviation column 
        -> An input of FL would return Florida. 
        This function should also take a boolean (`abbr_2_state`) and when `False` takes 
        full state names and return state abbreviations. -> An input of Florida would return Fl.

        Args:
            abbr_2_st (bool, optional): Defaults to True.

        Example Input (state_series = pd.Series):
        > | states     |
        > | ---------- |
        > | Alabama    |
        > | Arizona    |
        > | California |
        > | Delaware   |
        > | Ohio       |

        Function:
        > `abbr_2_st(state_series, abbr_2_st=False)`

        Expected Output (pd.Series): 
        > | st_2_abbr     |
        > | ------------- |
        > | AL            |
        > | AZ            |
        > | CA            |
        > | DE            |
        > | OH            |
        """
        pass

    def split_dates(self):
        """
        split_dates Function to split dates of format "MM/DD/YYYY" into multiple 
        columns (df['month'], df['day'], df['year']) and then return the same 
        dataframe with those additional columns.

        Example Input (date_series = pd.Series):
        > | column 0    |
        > | ----------- |
        > | 02/28/2006  |
        > | 03/09/2010  |
        > | 06/12/1850  |

        Function:
        > `split_dates(date_series)`

        Example Output (df = pd.DataFrame):
        > | month       | day         | year        |
        > | ----------- | ----------- | ----------- |
        > | 02          | 28          | 2006        |
        > | 03          | 09          | 2010        |
        > | 06          | 12          | 1850        |
        """
        df = pd.DataFrame()
        df['month'] = self.series.apply(lambda x: x.split('/')[0])
        df['day'] = self.series.apply(lambda x: x.split('/')[1])
        df['year'] = self.series.apply(lambda x: x.split('/')[2])
        return df
   
    def list_2_series(self):
        """
        list_2_series Single function to take a list and dataframe then turn the list 
        into a series and add it to the inputted dataframe as a new column.
        Example Input (list):
        > `[0, 1, 2]`

        Function:
        > `list_2_series(list, pd.DataFrame())`

        Expected Output (pd.Dataframe):  
        > | list          |
        > | ------------- |
        > | 0             |
        > | 1             |
        > | 2             |
        """
        self.series = pd.Series(self.series)
        self.df = pd.concat(self.df, self.series, axis=1)
        return self.df