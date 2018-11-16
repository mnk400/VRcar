import paho.mqtt.client as mqtt

mqtt = mqtt.Client()
mqtt.connect("192.168.0.8", 1883)

while True:
	var=input()
	if var == 'low':
		mqtt.publish("DriveChannel", "5")
	if var == 'mid':
		mqtt.publish("DriveChannel", "6")
	if var == 'high':
		mqtt.publish("DriveChannel", "7")