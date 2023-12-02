import matplotlib.pyplot as plt

def calorie_hist(dataframe):
    """ 
    Argument : A dataframe with a column "calories"
    Return : A pie chart showing the distribution of dishes according to their calorie content 
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
