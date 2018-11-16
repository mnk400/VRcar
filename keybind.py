from pynput import keyboard as key
import serial

ser = serial.Serial('/dev/cu.usbmodem14401', 115200)
flagup=flagl=flagr=flagd=0
def on_key_release(key):
    global flagup, flagl, flagr, flagd

    if (str(key) == "Key.up"):
        flagup=0
        print("Stop")
        ser.write('0'.encode())
    if (str(key) == "Key.left"):
        flagl=0
        print("Stop")
        ser.write('0'.encode())    
    if (str(key) == "Key.right"):
        flagr=0
        print("Stop")
        ser.write('0'.encode())    
    if (str(key) == "Key.down"):
        flagr=0
        print("Stop")
        ser.write('0'.encode())     

            


def on_key_press(key):
    global flagup, flagl, flagr, flagd

    if str(key) == "Key.up":
        if flagup<1:
            print("Up")
            ser.write('1'.encode())
            flagup=flagup+1
    if str(key) == "Key.left":
        if flagl<1:
            print("left")
            ser.write('3'.encode())
            flagl=flagl+1
    if str(key) == "Key.right":
        if flagr<1:
            print("right")
            ser.write('2'.encode())
            flagr=flagr+1
    if str(key) == "Key.down":
        if flagr<1:
            print("down")
            ser.write('4'.encode())
            flagd=flagd+1           


with key.Listener(on_release = on_key_release, on_press = on_key_press) as listener:
    listener.join()




