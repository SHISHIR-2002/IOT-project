import conf                 # importing configuration file
import time                 # module for sleep operation
import json                 # library for handling JSON data
from boltiot import Bolt    # importing Bolt from boltiot module      
mybolt=Bolt(conf.bolt_api_key,conf.device_id)


def ldr_value():            #the ldr_value function returns the ldr value
"""Returns the current light intensity value. Returns -55 if request fails"""  
    try:
        response=mybolt.analogRead('A0')      # reading the value from A0 pin and storing it in response variable
        data=json.loads(response)             # storing the response value into data
        if data["success"]!=1:
            print("request not successful")
            print("this is response",data)
            return -55
        sensor_value=int(data["value"])
        return sensor_value
    except Exception as e:
        print("something went wrong")
        print(e)
        return -55
      
while True:
    sensor_value=ldr_value()         #calling the ldr_value() function and storing it in sensor_value
    print("the current light intensity is :",sensor_value)

    if sensor_value == -55:
      """if any error occurs this block if code is executed"""
        print("there is an error the request is unsuccessfull")


    if sensor_value <= conf.threshold:              # if the sensor_value is lower than the threshold value then this block is executed 
        print("it is dark so turning the led on")   
        response=mybolt.digitalWrite(0,'HIGH')      # turning the led ON
        print(response)
        time.sleep(5)
        continue

    if sensor_value > conf.threshold:               # if the sensor_value is lower than the threshold value then this block is executed 
        print("it is not too dark so led is turning off")
        response=mybolt.digitalWrite(0,'LOW')       # turning the led OFF
        print(response)
        time.sleep(5)
        continue
    time.sleep(5)
