from operator import is_
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from turtle import speed
import serial
import time
import cv2
from PIL import Image, ImageTk
import pygame

import numpy as np


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)





#Layout 
########################################################################################################################
class App:
    window = Tk()
    window.geometry("1157x746")
    window.configure(bg = "#FFFFFF")
    window.resizable(False, False)
    window.title('Dashboard - WRO 2022')

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 746,
        width = 1157,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)






    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        101.0,
        373.0,
        image=image_image_1
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        bg="#008DF3",
        highlightthickness=0,
        command=lambda: print("df") ,   #open settings window
        relief="flat"
    )
    button_2.place(
        x=21.0,
        y=311.0,
        width=160.0,
        height=132.0
    )
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        bg="#008DF3",
        highlightthickness=0,
        command=lambda:lambda: print("df") ,
        relief="flat"
    )
    button_3.place(
        x=21.0,
        y=515.0,
        width=160.0,
        height=122.0
    )
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        bg="#008DF3",
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=21.0,
        y=139.0,
        width=160.0,
        height=126.0
    )

class dashboard :
    app = App()

    s= app.canvas.create_text(
        804.0,
        25.0,
        anchor="nw",
        text="Sensors :",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 31 * -1)
    )
    c= app.canvas.create_text(
        271.0,
        26.0,
        anchor="nw",
        text="Camera :",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 31 * -1)
    )




    Heartbeat_Text = app.canvas.create_text( #174
        804.0,
        123.0,
        anchor="nw",
        text="Heartbeat sensor :      " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    AmbientTemperature_Text =  app.canvas.create_text(
        804.0,
        225.0,
        anchor="nw",
        text="Ambient temperature :    " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    BodyTemperature_Text = app.canvas.create_text(
        804.0,
        327.0,
        anchor="nw",
        text="Body temperature  :      " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    Gyro_Text =app. canvas.create_text(
        804.0,
        378.0,
        anchor="nw",
        text="Gyro(xyz axis)  :      " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    Speed_Text = app.canvas.create_text(
        804.0,
        429.0,
        anchor="nw",
        text="Speed(m/s) :      " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    CO2Rate_Text =app. canvas.create_text(
        804.0,
        174.0,
        anchor="nw",
        text="CO2 level :      " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    AmbientHumidity_Text =app. canvas.create_text(
        804.0,
        276.0,
        anchor="nw",
        text="Ambient Humidity :     " + str(0) + "\n",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )



    Heartbeat_Warning = app.canvas.create_text( 
        804.0,
        489.0,
        anchor="nw",
        text="\n",
        fill="#D0342C",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    CO2_Warning = app.canvas.create_text( 
        804.0,
        509.0,
        anchor="nw",
        text="\n",
        fill="#D0342C",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    TBody_Warning = app.canvas.create_text( 
        804.0,
        529.0,
        anchor="nw",
        text="\n",
        fill="#D0342C",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    Gyro_Warning = app.canvas.create_text( 
        804.0,
        549.0,
        anchor="nw",
        text="\n",
        fill="#D0342C",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    speed_Warning =app. canvas.create_text( 
        804.0,
        589.0,
        anchor="nw",
        text="\n",
        fill="#D0342C",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )

    # r = canvas.create_rectangle(
    #     261.0,
    #     80.0,
    #     778.0,
    #     629.0,
    #     fill="#0000FF",
    #     outline="")
    
    width, height = 450,450  # set the size of the frame
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    CamLabel = Label(app.window, height=549, width=517)
    CamLabel.place(x=261.0, y=80.0)


    def show_frame(self):


        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.CamLabel.imgtk = imgtk
        self.CamLabel.configure(image=imgtk)
        self.CamLabel.after(10, d.show_frame)

    def play_ringtone(self):
        pygame.mixer.init()
        pygame.mixer.music.load(relative_to_assets("ringtone.mp3"))
        pygame.mixer.music.play()


    def do_update(self):
        
        data = [np.random.randint(0, 100) for i in range(8)]
        #data = data.decode("utf-8")
        #data = data.split(",")
        print((data))
        if len(data) == 8:
            Heartbeat = data[0]
            CO2= data[1]
            AmbientTemperature = data[2]
            BodyTemperature = "-"
            AmbientHumidity = data[3]
            Gyro_x = data[4]
            Gyro_y = data[5]
            Gyro_z = data[6]



            self.app.canvas.itemconfig(d.Heartbeat_Text, text="Heartbeat sensor :      " + str(Heartbeat) + " BPM" +"\n")
            self.app.canvas.itemconfig(d.AmbientTemperature_Text, text="Ambient temperature :    " + str(AmbientTemperature) + " C" + "\n")
            self.app.canvas.itemconfig(d.BodyTemperature_Text, text="Body temperature  :      " + "-" +" C" + "\n")
            self.app.canvas.itemconfig(d.Gyro_Text, text="Gyro(xyz): " + str(Gyro_x) +"º, " +str(Gyro_y)+"º, " +str(Gyro_z) + "º\n")
            self.app.canvas.itemconfig(d.Speed_Text, text="Speed :      " + str("-") + " m/s" + "\n")
            self.app.canvas.itemconfig(d.CO2Rate_Text, text="CO2 level :      " + str(CO2) +" ppm" "\n")
            self.app.canvas.itemconfig(d.AmbientHumidity_Text, text="Ambient Humidity :     " + str(AmbientHumidity) +" g.kg-1"+ "\n") 

            
            if float(Heartbeat) < 60:   
                self.app.canvas.itemconfig(d.Heartbeat_Warning, text="Warning: heartbeat rate is low !" + "\n") 
                d.play_ringtone()
            elif float(Heartbeat) > 100:
                self.app.canvas.itemconfig(d.Heartbeat_Warning, text="Warning: heartbeat rate is high !" + "\n") 
                d.play_ringtone()
            else:
                self.app.canvas.itemconfig(d.Heartbeat_Warning, text="\n")
                

            if float(CO2) > 600:
                self.app.canvas.itemconfig(d.CO2_Warning, text="Warning: CO2 level is high !" + "\n")
                d.play_ringtone()
            elif float(CO2) < 300:
                self.app.canvas.itemconfig(d.CO2_Warning, text="Warning: CO2 level is low !" + "\n")
                d.play_ringtone()
            else:
                self.app.canvas.itemconfig(d.CO2_Warning, text="\n")
            
            # if float(data[2]) > 38:
            #     canvas.itemconfig(TBody_Warning, text="Warning: body temperature is high !" + "\n")
            #     #play_ringtone()
            
            # elif float(data[2]) < 35:
            #     canvas.itemconfig(TBody_Warning, text="Warning: body temperature is low !" + "\n")
            #     #play_ringtone()
            # else:
            #     canvas.itemconfig(TBody_Warning, text="\n")
            

            if float(Gyro_x) > 16 or float(Gyro_x)<-16 or float(Gyro_y)>16 or float(Gyro_y)<-16 :
                self.app.canvas.itemconfig(d.Gyro_Warning, text="Warning: The robot is not aligned " + "\n")
                d.play_ringtone()

            else:
                self.app.canvas.itemconfig(d.Gyro_Warning, text="\n")

            


        self.app.window.after(1000, d.do_update)

    def destroy(self): #destroy dashboard window
        self.app.canvas.delete(self.AmbientHumidity_Text)
        self.app.canvas.delete(self.AmbientTemperature_Text)
        self.app.canvas.delete(self.BodyTemperature_Text)
        self.app.canvas.delete(self.CO2Rate_Text)
        self.app.canvas.delete(self.Gyro_Text)
        self.app.canvas.delete(self.Heartbeat_Text)
        self.app.canvas.delete(self.Speed_Text)
        self.app.canvas.delete(self.Heartbeat_Warning)
        self.app.canvas.delete(self.CO2_Warning)
        self.app.canvas.delete(self.TBody_Warning)
        self.app.canvas.delete(self.Gyro_Warning)
        self.app.canvas.delete(self.speed_Warning)
        #canvas.delete(self.r)
        self.app.canvas.delete(self.s)
        self.app.canvas.delete(self.c)
        self.app.window.destroy()

        
      

 
        


d = dashboard()
d.show_frame()
d.do_update()





d.app.window.mainloop()