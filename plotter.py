

import string
import numpy as np
import pandas as pd
import sklearn
import warnings
import seaborn as sns
warnings.filterwarnings('ignore')

from matplotlib import pyplot as plt
"""
This class contains methods for visualizing data about movies and TV shows.

Attributes:
    df (pandas.DataFrame): A dataframe containing information about movies and TV shows.
    title (str): The title for the plot.
    img_fmt (str): The image format for the plot.

Methods:
    plot(): Creates a barplot of the 10 most popular movie or TV show types, grouped by ratings.
    plot_top_countries(): Creates a barplot of the top countries where the movies or TV shows were produced.
    plot2(): Creates a barplot of the top 10 most productive directors.
"""

class MovieTVShowPlotter:
  def __init__(self, df, title, img_fmt):
    self.df = df
    self.title = title
    self.img_fmt=img_fmt

  def plot(self):
    fig,ax = plt.subplots(figsize = (10,10))
    #groupby ratings and tv show vs movie
    df_type_rating = self.df.groupby(['type','rating']).count().show_id.reset_index().sort_values(by = 'show_id').tail(10)
    #plot
    plots = sns.barplot(data = df_type_rating, x='type',y = 'show_id', hue = 'rating', palette='muted')
    #annotate the graph
    for bar in plots.patches:
            plots.annotate(format(bar.get_height(), '.0f'), 
                       (bar.get_x() + bar.get_width() / 2, 
                        bar.get_height() - (bar.get_height())/2), ha='center', va='center',
                       size=15, xytext=(0, 0),bbox=dict(boxstyle="round4,pad=0.6", fc="w", ec="red", lw=3),
                       textcoords='offset points')
            plt.box(on=None)
            plt.title(self.title, fontsize = 15, color = 'black')
            plt.xlabel('Type')
            plt.ylabel('Count')
            
    
  def plot_top_countries(self, title):
        countries = {}
        for country in self.df.country.dropna():
            for sub_country in str(country).split(', '):
                if sub_country not in countries:
                    countries[sub_country] = 1
                else: countries[sub_country] += 1
        df_countries = pd.DataFrame(list(countries.items()),columns = ['country','count']).sort_values(by = ['count'])

        plt.subplots(figsize = (10,8))
        plt.xticks(rotation = 60)
        plt.title(title, color='blue', fontsize=20)
        plots = sns.barplot(data = df_countries.tail()[::-1],x= 'country', y='count')
        for bar in plots.patches:
            plots.annotate(format(bar.get_height(), '.0f'), 
                           (bar.get_x() + bar.get_width() / 2, 
                            bar.get_height() - (bar.get_height()-3.1)/2), ha='center', va='center',
                           size=15, xytext=(0, 0),bbox=dict(boxstyle="round4,pad=0.6", fc="w", ec="black", lw=2),
                           textcoords='offset points')
        

    
  def plot2(self):
    
        movie = self.df[self.df['type'] == 'Movie']

        title = 'Top 10 most Productive Directors'
        _ = plt.figure(figsize=(18,8))
        _ = sns.barplot(y=movie.director.value_counts()[:10].sort_values().index,             x=movie.director.value_counts()[:10].sort_values().values);
        _ = plt.title(title, color='blue', fontsize=25)
        _ = plt.box(on=None)
        _ = plt.xticks(movie.director.value_counts()[:10].sort_values().values);
        _ = plt.xlim(min(movie.director.value_counts()[:10])-1,max(movie.director.value_counts()[:10])+1)
        plt.xlabel('Count of Total Movies Released');
       
