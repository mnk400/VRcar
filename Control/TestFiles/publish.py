import paho.mqtt.client as mqtt

mqtt = mqtt.Client()
mqtt.connect("Localhost", 1883)
mqtt.publish("DriveChannel", "Hello, World!")
 



