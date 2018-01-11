#pip install pandas
import pandas
import pandas as pd

my_dataframe = pd.read_csv("output.csv", encoding='utf-8', delimiter='|')

my_dataframe.capias = = my_dataframe.description.apply(lambda x: "CAPIAS" in x)

my_dataframe.indigency = my_dataframe.description.apply(lambda x: "INABILITY PAY COSTS" in x)

a = my_dataframe[my_dataframe.ncp_atty == 1]

capias_count = len(my_dataframe[my_dataframe.capias == 1])
#number of events

capias_count = len(set(my_dataframe[my_dataframe.capias == 1].ncp))
#number of people

capias_id_count = len(set(my_dataframe[my_dataframe.capias == 1].id))
#number of cases

my_dataframe['capias'] = my_dataframe.description.apply(lambda x: "1" if "CAPIAS" in x else "0")
#add capias as a column 
my_dataframe.to_csv("my_dataframe.csv")
#convert to csv
my_dataframe.to_csv("my_dataframe.csv", index=False)
#get rid of row numbers

my_dataframe.groupby(['ncp'])['id'].nunique()
#find number of cases that each person has 