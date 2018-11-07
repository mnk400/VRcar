import paho.mqtt.client as mqtt
import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', 115200)

def on_connect(client, userdata, rc):
	print("connected")

def on_message(client, userdata, msg):
	read = str(msg.payload)
	if read[2] == '1':
			print("Up")
			ser.write('1'.encode())

	if read[2] == '3':
			print("left")
			ser.write('3'.encode()) 

	if read[2] == '2':
			print("right")
			ser.write('2'.encode())

	if read[2] == '4':
			print("down")	
			ser.write('4'.encode())			

	if read[2] == '0':
			print("stop")
			ser.write('0'.encode())		





client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("Localhost", 1883, 60)
client.subscribe("DriveChannel")

client.loop_forever()
