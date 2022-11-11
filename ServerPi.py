
# pip3  install Adafruit_Python_DHT
# pip3 install Flask
# pip3 install Flask-RESTful

try:
    from flask import Flask
    from flask_restful import Resource,Api
    from flask_restful import reqparse
    from flask import request
    import time
    import datetime
    import json
    import Adafruit_DHT
    import random
    print("All modules loaded ")
except Exception as e:
    print("Error: {}".format(e))

import RPi.GPIO as GPIO 
import time 

"""
Sensor | TRIG | ECHO
1	 21	20
2	 16	12
3	 26	6
4	 25	1
5	 11	5
6	 10	9
"""



GPIO.setmode(GPIO.BCM) 

app = Flask(__name__)
api = Api(app)

#################################
#setup Sensor 1
GPIO_TRIG_1 = 21 
GPIO_ECHO_1 = 20
GPIO.setup(GPIO_TRIG_1, GPIO.OUT) 
GPIO.setup(GPIO_ECHO_1, GPIO.IN) 
GPIO.output(GPIO_TRIG_1, GPIO.LOW) 

#setup Sensor 2
GPIO_TRIG_2 = 16
GPIO_ECHO_2 = 12
GPIO.setup(GPIO_TRIG_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)
GPIO.output(GPIO_TRIG_2, GPIO.LOW)

#setup Sensor 3

GPIO_TRIG_3 = 26
GPIO_ECHO_3 = 6
GPIO.setup(GPIO_TRIG_3, GPIO.OUT)
GPIO.setup(GPIO_ECHO_3, GPIO.IN)
GPIO.output(GPIO_TRIG_3, GPIO.LOW)

#setup Sensor 4
GPIO_TRIG_4 = 25
GPIO_ECHO_4 = 1
GPIO.setup(GPIO_TRIG_4, GPIO.OUT)
GPIO.setup(GPIO_ECHO_4, GPIO.IN)
GPIO.output(GPIO_TRIG_4, GPIO.LOW)

#setup Sensor 5
GPIO_TRIG_5 = 11
GPIO_ECHO_5 = 5
GPIO.setup(GPIO_TRIG_5, GPIO.OUT)
GPIO.setup(GPIO_ECHO_5, GPIO.IN)
GPIO.output(GPIO_TRIG_5, GPIO.LOW)

#setup Sensor 6
GPIO_TRIG_6 = 10
GPIO_ECHO_6 = 9
GPIO.setup(GPIO_TRIG_6, GPIO.OUT)
GPIO.setup(GPIO_ECHO_6, GPIO.IN)
GPIO.output(GPIO_TRIG_6, GPIO.LOW)

def getDistance(GPIO_TRIG, GPIO_ECHO):
	GPIO.output(GPIO_TRIG, GPIO.HIGH) 
	time.sleep(0.00001) 
	GPIO.output(GPIO_TRIG, GPIO.LOW) 

	while GPIO.input(GPIO_ECHO) == 0: 
		pulse_start = time.time() 

	while GPIO.input(GPIO_ECHO) == 1: 
		pulse_end = time.time() 

	pulse_duration = pulse_end - pulse_start 
	distance = pulse_duration * 17150 
	distance = round(distance, 2) 
	return distance



class Sensors(object):

    def __init__(self):
        pass

    def get(self):
        try:
            #get request time
            now = datetime.datetime.now()

            return{
                'time': now.strftime("%H:%M:%S"),
                'S1':getDistance(GPIO_TRIG_1, GPIO_ECHO_1),
                'S2':getDistance(GPIO_TRIG_2, GPIO_ECHO_2),
                'S3':getDistance(GPIO_TRIG_3, GPIO_ECHO_3),
                'S4':getDistance(GPIO_TRIG_4, GPIO_ECHO_4),
                'S5':getDistance(GPIO_TRIG_5, GPIO_ECHO_5),
                'S6':getDistance(GPIO_TRIG_6, GPIO_ECHO_6),        
            }
        finally:
            pass


class Controller(Resource):
    def __init__(self):
        pass

    def get(self):
        helper = Sensors()
        return helper.get()


api.add_resource(Controller, "/")


if __name__ == "__main__":
    app.run(host='0.0.0.0')