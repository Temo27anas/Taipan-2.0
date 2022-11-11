import keyboard, serial,time, pandas as pd
import datetime

vexser = serial.Serial('COM8', 9600) ######################################################## 

mapping_active = True
i=0

#data frame of mapping
mapping = pd.DataFrame(columns=['time','h'])

#set time as index
mapping.set_index('time', inplace=True)


print("Mapping Active")


while True:

    if keyboard.is_pressed('o'):
        vexser.write(b'o')
        time.sleep(0.1)
    elif keyboard.is_pressed('l'):
        vexser.write(b'l')
        time.sleep(0.1)

    if keyboard.is_pressed('m'):
        
        #save mapping to csv
        mapping.to_csv('mapping.csv')
        print('mapping saved')
    

        
        
    
    #get current time 
    now = datetime.datetime.now()
    #read from serial port
    if vexser.inWaiting() > 0:
        data = vexser.readline().decode('utf-8').strip()
        if mapping_active:
            #add data to column h of mapping

            timeindex = now.strftime("%H:%M:%S")
            #put data in the h column of mapping
            mapping.loc[timeindex,'h'] = data
            
            #print(mapping)
    

