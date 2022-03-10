import numpy as np
import pandas as pd

def square(arr):
    return arr**2

def get_pi():
    return np.pi

def picky(num):
    if not isinstance(num, (np.float, float, np.int, int)):
        raise TypeError("Must input a number")

def read_df(path, delimiter=','):
    df = pd.read_table(path, usecols=[0,1,2], delimiter=delimiter, names=['year', 'y', 'y_err'])
    df['day'] = (df['year'] - 1973) * 366.242
    return df


