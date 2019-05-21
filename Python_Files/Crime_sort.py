# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:49:37 2018

@author: Levi
"""

import pandas as pd 

# This code separates the intial crime csv file into 5 separate csv files
# for the selected neighborhoods

# Just need to save csv file in same folder as py file
crime_report = pd.read_csv('crime.csv')
size = len(crime_report)


# Create empy dataframes for each neighborhood
auraria = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])

capitol_hill = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 

cbd = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC']) 

civic_center = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])  

lincoln_park = pd.DataFrame(columns=['INCIDENT_ID', 'OFFENSE_ID', 'OFFENSE_CODE', 'OFFENSE_CODE_EXTENSION',
       'OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE',
       'LAST_OCCURRENCE_DATE', 'REPORTED_DATE', 'INCIDENT_ADDRESS', 'GEO_X',
       'GEO_Y', 'GEO_LON', 'GEO_LAT', 'DISTRICT_ID', 'PRECINCT_ID',
       'NEIGHBORHOOD_ID', 'IS_CRIME', 'IS_TRAFFIC'])  

neighborhood_id = crime_report.iloc[:,16]

# Move the crime data according to each neighborhood
for i in range(size):
    
    if neighborhood_id[i] == 'auraria':
        auraria = auraria.append(crime_report.loc[i,:], ignore_index = True)
        
    elif neighborhood_id[i] == 'captiol_hill':
        capitol_hill = capitol_hill.append(crime_report.loc[i,:], ignore_index = True)
    
    elif neighborhood_id[i] == 'cbd':
        cbd = cbd.append(crime_report.loc[i,:], ignore_index = True)
        
    elif neighborhood_id[i] == 'civic_center':
        civic_center = civic_center.append(crime_report.loc[i,:], ignore_index = True)
        
    elif neighborhood_id[i] == 'lincoln-park':
        lincoln_park = lincoln_park.append(crime_report.loc[i,:], ignore_index = True) 
        
        
# Save the files back to csv form 
auraria.to_csv('Neighborhood Files/auraria.csv')
capitol_hill.to_csv('Neighborhood Files/capitol_hill.csv')
cbd.to_csv('Neighborhood Files/cbd.csv')
civic_center.to_csv('Neighborhood Files/civic-center.csv')
lincoln_park.to_csv('Neighborhood Files/lincoln_park.csv')