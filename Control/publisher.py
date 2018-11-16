from pynput import keyboard as key
import paho.mqtt.client as mqtt
import time

mqtt = mqtt.Client()
mqtt.connect("192.168.00.8", 1883)

flagup=flagl=flagr=flagd=0

def on_connect(client, userdata, flags, rc):
	print("Connected")

def on_key_release(key):
    global flagup, flagl, flagr, flagd

    if (str(key) == "Key.up"):
        flagup=0
        print("Stop")
        mqtt.publish("DriveChannel",0)
    if (str(key) == "Key.left"):
        flagl=0
        print("Stop")
        mqtt.publish("DriveChannel",0) 
    if (str(key) == "Key.right"):
        flagr=0
        print("Stop")
        mqtt.publish("DriveChannel",0) 
    if (str(key) == "Key.down"):
        flagd=0
        print("Stop")
        mqtt.publish("DriveChannel",0)     

            


def on_key_press(key):
    global flagup, flagl, flagr, flagd

    if str(key) == "Key.up":
        if flagup<1:
            print("Up")
            mqtt.publish("DriveChannel",1)
            flagup=flagup+1
    if str(key) == "Key.left":
        if flagl<1:
            print("left")
            mqtt.publish("DriveChannel",2)
            flagl=flagl+1
    if str(key) == "Key.right":
        if flagr<1:
            print("right")
            mqtt.publish("DriveChannel",3)
            flagr=flagr+1
    if str(key) == "Key.down":
        if flagd<1:
            print("down")
            mqtt.publish("DriveChannel",4)
            flagd=flagd+1     


with key.Listener(on_release = on_key_release, on_press = on_key_press) as listener:
    listener.join()
