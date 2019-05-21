# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:12:28 2018

@author: Levi
"""

import pandas as pd
# This file writes the data into a data.js file for the web page 
# Need to add the final function at the end 


file = open('data.js', 'w')
file.write("var data_topass = \n")



neighborhoods = ['auraria', 'capitol_hill' ,'cbd', 'civic_center', 'lincoln_park']
for k in neighborhoods:
    string = 'Neighborhood Files/' + k +'.csv'
    neighborhood_report = pd.read_csv(string)
    size = len(neighborhood_report)


    time = neighborhood_report.iloc[:,9]
    crime = neighborhood_report.iloc[:,6]
    file.write("{\n")
    file.write("'" + k + "' : {\n")

    crimes = ['aggravated-assault', 'drug-alcohol', 'robbery']


    for j in crimes:
        file.write("'" + j + "'" + " " + ":" + " " + "[")
        comma = 0
        for i in range(size):
    
            time1 = time[i]
            val = time1.split()
            val2 = val[0].split('/')
            

            # Pull data from the last month
            if (val2[0] == '11' and val2[2] == '2018' and crime[i] == j): 
                if comma != 0:
                    file.write(', ')
            
                string = "'Crime:" + " " + str(neighborhood_report.iloc[i,5]) + " " + "Date:" + " " + str(neighborhood_report.iloc[i,9]) + " " + "Address:" + " " + str(neighborhood_report.iloc[i,10]) + "'"
                string = str(string)
                file.write(string)
                comma = 1
        file.write("]\n")
    file.write("},\n \n") 
        
file.write("}")
file.close()
    
