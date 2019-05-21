# -*- coding: utf-8 -*-
"""
Spyder Editor

Levi Nickerson
Crime Project
"""
import pandas as pd 

# Code currently takes a long time to run
# It is parsing through over 500,000 crimes
# Need to see if we can get it to run faster

# Just need to save csv file in same folder as py file
crime_report = pd.read_csv('crime.csv')
size = len(crime_report)

# Pull out all of the desired columns 
# Can eventually add GEO info if we want to
district_id = crime_report.iloc[:,14]
precinct_id = crime_report.iloc[:,15]
neighborhood_id = crime_report.iloc[:,16]
offense_category = crime_report.iloc[:,5]
offense_code = crime_report.iloc[:,2]
occurrence_date = crime_report.iloc[:,6] 



# Set up vectors for date splitting 
month = [0]*size
day = [0]*size
year = [0]*size

# Set up storage vector 
neighborhood = [0]*size

# Set up storage vector
offense = [0]*size

# Date splitting
# Month, day, and year can now be used to correctly process
# specific date queries  
for i in range(size):
    
# Date splitting
# Month, day, and year can now be used to correctly process
# specific date queries       
    temp = occurrence_date[i]
    temp_s = temp.split()
    temp_ss = temp_s[0].split("/")
    month[i] = int(temp_ss[0])
    day[i] = int(temp_ss[1])
    year[i] = int(temp_ss[2])
    
# Can now use month, day, and year to handl day queries
# Can come up with date bounds to generate html pages off of 

# Neighborhood splitting
# Parse through database and split into various neighborhoods 
    if (neighborhood_id[i] == 'belcaro'):
        neighborhood[i] = 1
    
    elif (neighborhood_id[i] == 'cherry-creek'):
        neighborhood[i] = 2
        
    elif (neighborhood_id[i] == 'gateway-green-valley-ranch'):
        neighborhood[i] = 3
        
    elif (neighborhood_id[i] == 'montbello'):
        neighborhood[i] = 4
        
    elif (neighborhood_id[i] == 'wellshire'):
        neighborhood[i] = 5
        
# Base code is ready to pull values based on neighborhood id
# Have only included 5, but can add all of them if needed   

# Offense splitting
# Parse through database and split into various offenses 
    if (offense_category[i] == 'murder'):
        offense[i] = 1
    
    elif (offense_category[i] == 'robbery'):
        offense[i] = 2
        
    elif (offense_category[i] == 'aggravated-assault'):
        offense[i] = 3
        
    elif (offense_category[i] == 'arson'):
        offense[i] = 4
        
    elif (offense_category[i] == 'larceny'):
        offense[i] = 5
        
# Base code is set up to handle queries 
