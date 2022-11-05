import keyboard, serial,time

vexser = serial.Serial('COM8', 9600)


while True:

    if keyboard.is_pressed('o'):
        vexser.write(b'o')
        time.sleep(0.1)
    elif keyboard.is_pressed('l'):
        vexser.write(b'l')
        time.sleep(0.1)


