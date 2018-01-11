#pip install pandas
import pandas
import pandas as pd

my_dataframe = pd.read_csv("output.csv", encoding='utf-8', delimiter='|')

my_dataframe.capias = my_dataframe.description.apply(lambda x: "CAPIAS" in x)

my_dataframe.indigency = my_dataframe.description.apply(lambda x: "INABILITY PAY COSTS" in x)
my_dataframe.bond = my_dataframe.description.apply(lambda x: "BOND" in x)
my_dataframe.warrant = my_dataframe.description.apply(lambda x: "WARRANT" in x)
my_dataframe.commit = my_dataframe.description.apply(lambda x: "COMMIT" in x)
my_dataframe.cost = my_dataframe.description.apply(lambda x: "COST" in x)
my_dataframe.revoke = my_dataframe.description.apply(lambda x: "REVOKE" in x)
my_dataframe.appt = my_dataframe.description.apply(lambda x: "APPOINTMENT AG" in x)
my_dataframe.enf = my_dataframe.description.apply(lambda x: "ENFORCE" in x)
my_dataframe.noservice = my_dataframe.description.apply(lambda x: "UNEXECUTED RETURN" in x)

a = my_dataframe[my_dataframe.ncp_atty == 1]

capias_count = len(my_dataframe[my_dataframe.capias == 1])
#number of events

indigency_count = len(my_dataframe[my_dataframe.indigency == 1])
bond_count = len(my_dataframe[my_dataframe.bond == 1])
warrant_count = len(my_dataframe[my_dataframe.warrant == 1])
commit_count = len(my_dataframe[my_dataframe.commit == 1])
cost_count = len(my_dataframe[my_dataframe.cost == 1])
revoke_count = len(my_dataframe[my_dataframe.revoke == 1])
appt_count = len(my_dataframe[my_dataframe.appt == 1])
enf_count = len(my_dataframe[my_dataframe.enf == 1])
noservice_count = len(my_dataframe[my_dataframe.noservice == 1])

capias_ppl_count = len(set(my_dataframe[my_dataframe.capias == 1].ncp))
#number of people

indigency_ppl_count = len(set(my_dataframe[my_dataframe.indigency == 1].ncp))
bond_ppl_count = len(set(my_dataframe[my_dataframe.bond == 1].ncp))
warrant_ppl_count = len(set(my_dataframe[my_dataframe.warrant == 1].ncp))
commit_ppl_count = len(set(my_dataframe[my_dataframe.commit == 1].ncp))
cost_ppl_count = len(set(my_dataframe[my_dataframe.cost == 1].ncp))
revoke_ppl_count = len(set(my_dataframe[my_dataframe.revoke == 1].ncp))
appt_ppl_count = len(set(my_dataframe[my_dataframe.appt == 1].ncp))
enf_ppl_count = len(set(my_dataframe[my_dataframe.enf == 1].ncp))
noservice_ppl_count = len(set(my_dataframe[my_dataframe.noservice == 1].ncp))

capias_id_count = len(set(my_dataframe[my_dataframe.capias == 1].id))
#number of cases

indigency_id_count = len(set(my_dataframe[my_dataframe.indigency == 1].id))
bond_id_count = len(set(my_dataframe[my_dataframe.bond == 1].id))
warrant_id_count = len(set(my_dataframe[my_dataframe.warrant == 1].id))
commit_id_count = len(set(my_dataframe[my_dataframe.commit == 1].id))
cost_id_count = len(set(my_dataframe[my_dataframe.cost == 1].id))
revoke_id_count = len(set(my_dataframe[my_dataframe.revoke == 1].id))
appt_id_count = len(set(my_dataframe[my_dataframe.appt == 1].id))
enf_id_count = len(set(my_dataframe[my_dataframe.enf == 1].id))
noservice_id_count = len(set(my_dataframe[my_dataframe.noservice == 1].id))

my_dataframe['capias'] = my_dataframe.description.apply(lambda x: "1" if "CAPIAS" in x else "0")
#add capias as a column 

my_dataframe['indigency'] = my_dataframe.description.apply(lambda x: "1" if "INABILITY PAY COSTS" in x else "0")
my_dataframe['bond'] = my_dataframe.description.apply(lambda x: "1" if "BOND" in x else "0")
my_dataframe['warrant'] = my_dataframe.description.apply(lambda x: "1" if " WARRANT" in x else "0")
my_dataframe['commit'] = my_dataframe.description.apply(lambda x: "1" if "COMMIT" in x else "0")
my_dataframe['cost'] = my_dataframe.description.apply(lambda x: "1" if "COST" in x else "0")
my_dataframe['revoke'] = my_dataframe.description.apply(lambda x: "1" if "REVOKE" in x else "0")
my_dataframe['appt'] = my_dataframe.description.apply(lambda x: "1" if "APPOINTMENT AG" in x else "0")
my_dataframe['enf'] = my_dataframe.description.apply(lambda x: "1" if "ENFORCE" in x else "0")
my_dataframe['noservice'] = my_dataframe.description.apply(lambda x: "1" if "UNEXECUTED RETURN" in x else "0")


my_dataframe.to_csv("my_dataframe_working.csv")
#convert to csv
my_dataframe.to_csv("my_dataframe_working.csv", index=False)
#get rid of row numbers

my_dataframe.groupby(['ncp'])['id'].nunique()
#find number of cases that each person has 