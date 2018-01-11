import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats

from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

address = '~/Desktop/code/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars = pd.read_csv(address)

print(cars.head(10))

cars_groups = cars.groupby(cars['cyl'])
print(cars_groups.mean())

df = cars[['cyl', 'mpg','wt']]

df.plot()

#plt.show()

X = cars[['mpg', 'hp', 'qsec','wt']]
sb.pairplot(X)


mpg = cars['mpg']
hp = cars['hp']
qsec = cars['qsec']
wt = cars['wt']
cyl = cars['cyl']
vs = cars['vs']
am = cars['am']
gear = cars['gear']

pearsonr_coefficient, p_value = pearsonr(mpg, hp)
#calculate R for mpg and hp, and show p-value
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
#print label, with 3 decimal places: -0.77
pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
#0.419
pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print 'PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient)
# -.87

spearmanr_coefficient, p_value = spearmanr(cyl, vs)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.814
spearmanr_coefficient, p_value = spearmanr(cyl, am)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.522
spearmanr_coefficient, p_value = spearmanr(cyl, gear)
print 'Spearman Rank Correlation Coefficient %0.3f' % (spearmanr_coefficient)
#-0.56

#Chi2 test
table = pd.crosstab(cyl, am)
#call crosstab function on our 2 vars of inteerest

#import contingency function
chi2, p, dof, expected = chi2_contingency(table.values)
#we want chi2, p val, dof, and expected
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 8.741 p_value 0.013

table = pd.crosstab(cars['cyl'], cars['vs'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 21.340 p_value 0.000

table = pd.crosstab(cars['cyl'], cars['gear'])
chi2, p, dof, expected = chi2_contingency(table.values)
print 'Chi-square Statistic %0.3f p_value %0.3f' % (chi2, p)
#Chi-square Statistic 18.036 p_value 0.001