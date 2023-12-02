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
