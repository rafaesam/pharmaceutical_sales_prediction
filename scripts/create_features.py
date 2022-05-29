import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))

'''
This script is responsible for creating features for train and test data
'''
class CreateFeatures():
  '''
  Calculates evaluation metrics for a give model using actual data
  '''

  def __init__(self):
    self.store_df = pd.read_csv('../data/cleaned_store.csv')
    self.train_df = pd.read_csv('../data/cleaned_train.csv')
    self.test_df = pd.read_csv('../data/cleaned_test.csv')

  def get_part_of_month(self, date):
    if (date < 10):
      return 0
    elif(date < 20):
      return 1
    else:
      return 2

  def get_state_holiday_info(self, df):

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    days_after_state_holiday = []
    days_before_state_holiday = []

    num_days = 0
    for i in df['StateHoliday']:
      if(i == 1):
        num_days = 0
      else:
        num_days += 1
      days_after_state_holiday.append(num_days)

    small_list = []
    bigger_list = []
    for i in days_after_state_holiday:
      if(i == 0):
        small_list.reverse()
        bigger_list.append(small_list)
        bigger_list.append([0])
        small_list = []
      else:
        small_list.append(i)

    small_list.reverse()
    bigger_list.append(small_list)
    days_before_state_holiday = [item for sublist in bigger_list for item in sublist]

    df['days_before_state_holiday'] = days_before_state_holiday
    df['days_after_state_holiday'] = days_after_state_holiday
    return df

  def extract_features(self, df):
    df = df[df['Open'] != 0]

    # convert date column to datetime
    df = self.get_state_holiday_info(df)

    # Feature creation
    df['Year'] = df.Date.dt.year
    df['Month'] = df.Date.dt.month
    df['Day'] = df.Date.dt.day
    df['DayOfWeek'] = df.Date.dt.dayofweek
    df['WeekOfYear'] = df.Date.dt.weekofyear

    df['Weekends'] = df['DayOfWeek'].apply(lambda x: 1 if x >= 6 else 0)
    df['Weekdays'] = df['DayOfWeek'].apply(lambda x: 1 if x < 6 else 0)

    df["part_of_month"] = df["Day"].apply(self.get_part_of_month)

    # Combining similar columns into one column and dropping old columns
    df['CompetitionOpen'] = 12 * (df.Year - df.CompetitionOpenSinceYear) + (df.Month - df.CompetitionOpenSinceMonth)
    df.drop(["CompetitionOpenSinceYear", "CompetitionOpenSinceMonth"], axis=1, inplace=True)

    df['Promo2Open'] = 12 * (df.Year - df.Promo2SinceYear) + (df.WeekOfYear - df.Promo2SinceWeek) / 4.0
    df.drop(["Promo2SinceYear", "Promo2SinceWeek"], axis=1, inplace=True)

    df = df.set_index('Date')
    df = df.sort_index()
    return df

  def merge(self, df, store):
    df_merge = pd.merge(df, store, on='Store')
    return df_merge

  def extract_sales(self, df):
    return df[["Sales"]]

  def extract_customers(self, df):
    return df[["Customers"]]

  def create_features(self):
    train_data = self.merge(self.train_df, self.store_df)
    train_features = self.extract_features(train_data)
    test_data = self.merge(self.test_df, self.store_df)
    test_features = self.extract_features(test_data)

    train_sales = self.extract_sales(train_features)
    train_customers = self.extract_customers(train_features)

    test_features.drop(["Store", "Open"], axis=1, inplace=True)
    train_features.drop(["Store", "Open", "Sales", "Customers"], axis=1, inplace=True)

    test_features.to_csv('../features/test_features.csv', index=False)
    train_features.to_csv('../features/train_features.csv', index=False)
    train_sales.to_csv('../features/train_sales.csv', index=False)
    train_customers.to_csv('../features/train_customers.csv', index=False)

x = CreateFeatures()
x.create_features()