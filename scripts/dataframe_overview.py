"""
This file will be responsible for overviewing data, like basic information how many unique values we have, ..etc
Number of classes : 1
Number of functions :  4
	missing_value
    unique_values
    percentage
    getOverview
"""

import pandas as pd
import logging
from logging import getLogger

logging.getLogger("dataframe_overview")
logging.debug("Yes it's working now!")

class DfOverview():
  """
      Give an overview for a given data frame, 
      like null persentage for each columns, 
      unique value percentage for each columns and more
  """

  def __init__(self, df: pd.DataFrame) -> None:
    """
    """
    self.df = df

  def missing_value(self) -> None:
    """here we sum all the missing values in any column
    """
    all_nulls = self.df.isna().sum()
    return [col for col in all_nulls]

  def unique_values(self) -> None:
    """this function is responsible of telling us the unique values in each column
    """
    return [self.getUniqueCount(column) for column in self.df]

  def percentage(self, list):
    """
    """
    return [str(round(((value / self.df.shape[0]) * 100), 2)) + '%' for value in list]

  def getOverview(self) -> None:
    """this will give us labels of columns, unique, count and missing values
    """
    _labels = [column for column in self.df]  # Only numeric columns
    _count = self.df.count().values
    _unique = [self.df[column].value_counts().shape[0] for column in self.df]
    _missing_values = self.missing_value()

    columns = [
      'label',
      'count',
      'null_count',
      'null_percentage',
      'unique_value_count',
      'unique_percentage',
      'dtype']
    data = zip(
      _labels,
      _count,
      _missing_values,
      self.percentage(_missing_values),
      _unique,
      self.percentage(_unique),
      self.df.dtypes
    )
    new_df = pd.DataFrame(data=data, columns=columns)
    new_df.set_index('label', inplace=True)
    new_df.sort_values(by=["null_count"], inplace=True)
    return new_df