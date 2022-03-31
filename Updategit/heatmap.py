# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:23:37 2020

@author: Maryam Botrus 
"""
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import csv
import numpy as np
import os
#os.mkdir('figures') # run if figures directory is not there
#import matplotlib


# set file names 
name = ['all-states-history.csv']

# first field is empty
# next fifty rows are the states 
# date is field 0 
# state is field 1 
# positive cases are field 20
# https://covidtracking.com/data/download/all-states-history.csv

counter = 0
state_data = []
state_list = []
with open(name[0]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row[1])
        counter = counter + 1 # iterator skip first element
        #counter = counter % 50 # handle 50 states
        my_date = row[0]
        if(counter > 1):
            state_data.append(np.log10(float(row[20])+1))
            state_list.append(row[1])
        if(len(state_data) == 56):
            fig = go.Figure(data=go.Choropleth(
                locations=state_list, # Spatial coordinates
                z = state_data,
                locationmode = 'USA-states', # set of locations match entries in `locations`
                #zmid= 50000,
                #zmin = 0,
                #zmax = 1200000,
                #coloraxis =np.log10(state_data),
                zmin=3,
                zmax=6.1,
                colorscale = 'Reds',
                colorbar_title = "Log10 Num. of Infections",
            ))
            
            fig.update_layout(
                title_text = '2020 US Coronavirus Outbreak Date: ' + my_date,
                geo_scope='usa', # just show a map of u.s states 
    )       
            #fig.data[0].update(zmin=0)
           
            fig.show(renderer="png", width=1200, height=1000)
            fig.update_layout(width=1200, height=1000)
            fig.write_image("figures/" + my_date + ".png")
            #plot(fig)
            state_data = []
            state_list = []