import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class NJCleaner():

    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self):
        self.data = self.data.sort_values(by=['scheduled_time'])
         
        return self.data
    
    def drop_columns_and_nan(self):
        self.data= self.data.drop(columns=['from', 'to']).dropna()        
        return self.data
    
    def convert_date_to_day(self):
        self.data['day'] = (pd.to_datetime(self.data['date'])).dt.day_name()
        self.data = self.data.drop(columns=['date'])
        
        return self.data
    
    def convert_scheduled_time_to_part_of_the_day(self):
        self.data['part_of_the_day'] = pd.to_datetime(self.data['scheduled_time']).dt.hour.apply(lambda time: 'early_morning' if time >= 4 and time < 8 else('morning' if time >= 8 and time < 12 else('afternoon' if time >= 12 and time < 16 else('evening' if time >= 16 and time < 20 else('night' if time >= 20 and time < 24 else('late_night'))))))
        self.data= self.data.drop(columns=['scheduled_time'])        
        return self.data
          
    def convert_delay(self):
        self.data['delay'] = self.data['delay_minutes'].apply(lambda x: 0 if x >= 0 and x < 5 else(1))
        return self.data
    
    def drop_unnecessary_columns(self):
        self.data = self.data.drop(columns=['train_id', 'actual_time', 'delay_minutes'])
        
        return self.data
    
    def save_first_60k(self,path):
        self.data.head(60000).to_csv(path)
        
    def prep_df(self, path = 'NJ.csv'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)

