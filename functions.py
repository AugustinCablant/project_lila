import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def calorie_hist(dataframe):
    """ 
    Argument : A dataframe with a column "calories"
    Return : An histogram showing the distribution of dishes according to their calorie content 
    """
    dataframe['tranche'] = (dataframe['calories'] // 50) * 50
    counts = dataframe['tranche'].value_counts().sort_index()
    plt.figure(figsize=(8,8))
    plt.hist(dataframe['tranche'], bins=range(0, int(dataframe['tranche'].max()) + 50, 50), edgecolor='black', alpha=0.7)
    plt.xlabel('Calories band')
    plt.ylabel('Number of recipies')
    plt.title('Breakdown of recipes by calorie band')
    plt.show()
    return None

def preparation_time(dataframe):
    """ 
    Argument : A dataframe with a column "calories"
    Return : An histogram showing the distribution of dishes according to their time preparation 
    """
    dataframe = dataframe.dropna(subset=['prep_time'])
    dataframe['prep_time'] = dataframe['prep_time'].str.extract('(\d+)').astype(float)
    dataframe['prep_time'] = dataframe['prep_time'].astype('Int64')
    plt.hist(dataframe['prep_time'], bins=range(0, dataframe['prep_time'].max() + 10, 10), edgecolor='black', alpha=0.7)
    plt.xlabel('In minutes')
    plt.ylabel('Number of recipies')
    plt.title('Distribution of recipes by preparation time')
    plt.show()
    return None

def extract_h_mins(row):
    """ 
    Argument : A row of a dataframe : "1 h 25 mins" for example
    Return : 85 (corresponding to the number of minutes) 
    """
    row = row.replace("hrs","hr")
    if row != np.nan:
        parts = row.split('hr')
        n = len(parts)  #2 if there is an hour and 1 else
        if n==1: 
            min = parts[0]
            hour_in_mins = float(min.split('mins')[0].strip())
        else: 
            hour = float(parts[0].strip()) 
            mins_str = parts[1].split("mins")[0].strip()
            if len(mins_str)>0:
                mins = float(mins_str) 
            else: mins = 0
            hour_in_mins = hour * 60 + mins
        return hour_in_mins 
    else: 
        return row

def cook_time(dataframe):
    """ 
    Argument : A dataframe with a column "calories"
    Return : An histogram showing the distribution of dishes according to their cooking time preparation 
    """
    dataframe = dataframe.dropna(subset=['cook_time'])
    dataframe['cook_time'] = dataframe['cook_time'].apply(extract_h_mins)
    dataframe['cook_time'] = dataframe['cook_time'].astype('Int64')
    plt.hist(dataframe['prep_time'], bins=range(0, dataframe['prep_time'].max() + 10, 10), edgecolor='black', alpha=0.7)
    plt.xlabel('In minutes')
    plt.ylabel('Number of recipies')
    plt.title('Distribution of recipes by preparation time')
    plt.show()
    return None
