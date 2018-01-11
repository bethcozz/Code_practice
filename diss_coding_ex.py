import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

from scipy.stats import spearmanr
from scipy.stats import chi2_contingency

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

address = "~/Desktop/code/diss_data.csv"
my_dataframe = pd.read_csv(address)

my_dataframe['anyjail'] = my_dataframe.description.apply(lambda x: "1" if "CAPIAS" or "BOND" or "WARRANT" in x else "0")

def label_anyjail (row):
    if row['capias'] + row['bond'] + row['warrant']  >= 1 :
        return '1'
    if row['capias'] + row['bond'] + row['warrant'] = 0:
        return '0'


my_dataframe.head()