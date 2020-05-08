"""
Created on Fri Mar 16 16:31:37 2018

@author: james
"""
import pandas as pd


def map_csv(filename=''):
    df = pd.read_csv(filename, index_col='')

    # Create the dictionary: red_vs_blue
    dictionary = {'': ''}

    # Where the winner column matches the value in a dictionary, put the dict value
    # to a new column called 'colour
    df['colour'] = df['winner'].map(dictionary)
