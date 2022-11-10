import requests
import time
import pandas as pd
import keyboard
url = 'http://10.126.164.183:5000/'

#create a pandas dataframe
sensorsdata = pd.DataFrame(columns=['time', 'S1', 'S2', 'S3','S4','S5','S6'])
#set time as index
sensorsdata.set_index('time', inplace=True)




while(1): 



    r = requests.get(url)  
    #decompose the json data
    datareq = r.json()
    
    timeindex = datareq['time']
    #put data in the h column of mapping
    sensorsdata.loc[timeindex,'S1'] = datareq['S1']
    sensorsdata.loc[timeindex,'S2'] = datareq['S2']
    sensorsdata.loc[timeindex,'S3'] = datareq['S3']
    sensorsdata.loc[timeindex,'S4'] = datareq['S4']
    sensorsdata.loc[timeindex,'S5'] = datareq['S5']
    sensorsdata.loc[timeindex,'S6'] = datareq['S6']

    #print(sensorsdata)

    if keyboard.is_pressed('a'):
        #save mapping to csv
        sensorsdata.to_csv('sensorsdata.csv')
        print('mapping saved')
        time.sleep(0.1)




    time.sleep(0.5)
    #sensorsdata.loc[timeindex,'h'] = data

    



    