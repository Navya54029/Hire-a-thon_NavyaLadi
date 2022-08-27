# Hire-a-thon_NavyaLadi

Problem Statement - Employee Performance problem statement

# Description

Used Python pandas dataframe to read the data from excel.
config.py contains the intial dataframe
solution.py contains the code required for problem statement.


 1) Mean effort spent by various teams on different projects
            Approach for the problem is, I have separated out the unique projects and unique teams in the dataframe. And then Calculated mean hours spent by employees for all teams and projects.
            
 2) 5 employees with the lowest efficiency
            Approach for the sub problem is, I have created a new dataframe from the source dataframe with "Project Name, Owner and Hours" columns and then calculated mean for every team member in all projects. And then sorted the result and printed the first 5 lowest hours spent employees.
            
# Prerequisite

1) Python
2) Libraries like Pandas,Numpy

# How to run

1) git pull the repository
2) cd into "Employee Performance problem statement"
3) Run python solution.py