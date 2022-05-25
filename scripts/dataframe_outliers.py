"""
This file will be responsible for overviewing data, like basic information how many unique values we have, ..etc
Number of classes : 1
Number of functions :  5
        count_outliers
        calc_skew
        remove_outliers
        replace_outliers_with_iqr
        outliers_overview
"""

import pandas as pd
import numpy as np
import logging
from logging import getLogger


class DfOutlier:
  """
    Give percentage of outliers in each column in our dataframe and has methods for removeing or replacing outliers.
  """

  def __init__(self, df: pd.DataFrame) -> None:
    """
    """
    self.df = df

  def count_outliers(self, Q1, Q3, IQR):
    """This is just to count how many outliers in the dataframe, dividing it by three ponts into 4 parts
    """
    Q2 = IQR * 1.5
    temp_df = (self.df < (Q1 - Q2)) | (self.df > (Q3 + Q2))
    return [len(temp_df[temp_df[col] == True]) for col in temp_df]

  def calc_skew(self):
    """this is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean
    """
    return [self.df[col].skew() for col in self.df]

  def remove_outliers(self, columns):
    """here we see how to move outliers
    """ 
    for col in columns:
      Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
      IQR = Q3 - Q1
      Q2 = IQR * 1.5
      lower, upper = Q1 - Q2, Q3 + Q2
      self.df = self.df.drop(self.df[self.df[col] > upper].index)
      self.df = self.df.drop(self.df[self.df[col] < lower].index)

  def replace_outliers_with_iqr(self, columns):
    """sometimes we don't simply move outliers but rather choose to replace them!
       this replacement here using interquartile range IQR
    """
    for col in columns:
      Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
      IQR = Q3 - Q1
      cut_off = IQR * 1.5
      lower, upper = Q1 - cut_off, Q3 + cut_off

      self.df[col] = np.where(self.df[col] > upper, upper, self.df[col])
      self.df[col] = np.where(self.df[col] < lower, lower, self.df[col])

  def outliers_overview(self) -> None:

    _labels = [column for column in self.df]
    Q1 = self.df.quantile(0.25)
    _median = self.df.quantile(0.5)
    Q3 = self.df.quantile(0.75)
    IQR = Q3 - Q1
    _skew = self.calc_skew()
    _outliers = self.count_outliers(Q1, Q3, IQR)

    columns = [
      'label',
      'number_of_outliers',
      'percentage_of_outliers',
      'skew',
      'Q1',
      'Median',
      'Q3'
    ]
    data = zip(
      _labels,
      _outliers,
      self.percentage(_outliers),
      _skew,
      Q1,
      _median,
      Q3,
    )
    new_df = pd.DataFrame(data=data, columns=columns)
    new_df.set_index('label', inplace=True)
    new_df.sort_values(by=["number_of_outliers"], inplace=True)
    return new_df