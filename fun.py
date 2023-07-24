
import pylab as plt
import seaborn as sns
import re
import pandas as pd


#Ploteo de valores nulos:

def nanplot(df):  
    
    plt.figure(figsize = (10, 6))
    sns.heatmap(df.isna(),
                yticklabels = False,
                cmap ='viridis',
                cbar = False,  
                )
    plt.show()
    
    