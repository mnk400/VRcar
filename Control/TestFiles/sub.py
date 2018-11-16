import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	print("connected")
	#client.subscribe("DriveChannel")

def on_message(client, userdata, msg):
	print("Topic: ", msg.topic+'\nMessage: '+str(msg.payload)) 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("Localhost", 1883, 60)
client.subscribe("test/topic")

client.loop_forever()
