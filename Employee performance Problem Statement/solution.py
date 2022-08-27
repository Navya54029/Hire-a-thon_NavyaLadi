from config import *
import numpy as np
from collections import OrderedDict


def lowest5performers():
    owner_dict = {}
    for owner in owner_names:
        temp_team_df = excel_data_df.loc[(excel_data_df["Owner"] == owner), ['Project Name','Owner', 'Hours']]
        mean = temp_team_df["Hours"].mean()
        if np.isnan(mean):
            pass
        else:
            owner_dict[owner] = mean

    # Sorting the dictionary based on values
    dictionary_keys = list(owner_dict.keys())
    sorted_dict = {dictionary_keys[i]: sorted(
        owner_dict.values())[i] for i in range(len(dictionary_keys))}
    
    print("5 Employees with Lowest Efficiency")
    first5pairs = {k: sorted_dict[k] for k in list(sorted_dict)[:5]}
    for key,value in first5pairs.items():
        print(key, value)

def meanCalculation(temp_team_df,project,team):
    return temp_team_df["Hours"].mean()

# Data Initialization
# Unique Projects
project_names = (excel_data_df["Project Name"].unique()).tolist()

# Unique Teams
team_names = (excel_data_df["Team"].unique()).tolist()

#Unique Owners
owner_names = (excel_data_df["Owner"].unique()).tolist()

print("Mean effort spent by various teams in on diffferent projects")
#Looping through all the existing Projects ans teams
# And it prints mean
for project in project_names:
    
    temp_project_df = excel_data_df.loc[(excel_data_df['Project Name'] == project), ['Project Name','Team', 'Hours']]
    for team in team_names:
        temp_team_df = temp_project_df.loc[(temp_project_df["Team"] == team), ['Project Name','Team', 'Hours']]
        mean = meanCalculation(temp_team_df,project,team)
        if np.isnan(mean):
            pass
        else:
            print('Project Name: {p}, Team: {t}, Mean: {m}'.format(p=project,t=team,m=mean))


lowest5performers()

