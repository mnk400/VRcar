import keyboard
import serial
ser = serial.Serial('/dev/cu.Bluetooth-Incoming-Port', 115200)
i = 0
while True:
        if keyboard.is_pressed('up'):
            print('You Pressed Up Key!')
            ser.write('3')
        if keyboard.is_pressed('down'):
            print('You Pressed Down Key!')
            ser.write('4')
        if keyboard.is_pressed('left'):
            print('You Piressed Left Key!')
            ser.write('1'.encode())
        if keyboard.is_pressed('right'):
            print('You Pressed Right Key!')
            ser.write('2'.encode())
        if keyboard.is_pressed('q'):
            print('Q Pressed. Exiting\n')
            break
        else:
            if i > 4:
                ser.write('0'.encode())
                i = 0
            i = i+1
            pass
