import keyboard
import serial
ser = serial.Serial('/dev/cu.usbmodem1451', 115200)
i = 0
while True:
        if keyboard.is_pressed('up'):
            print('You Pressed Up Key!')
            ser.write('3')
        if keyboard.is_pressed('down'):
            print('You Pressed Down Key!')
            ser.write('4')
        if keyboard.is_pressed('left'):
            print('You Pressed Left Key!')
            ser.write('1')
        if keyboard.is_pressed('right'):
            print('You Pressed Right Key!')
            ser.write('2')
        if keyboard.is_pressed('q'):
            print('Q Pressed. Exiting\n')
            break
        if keyboard.is_pressed('b'):
            if keyboard.is_pressed('a'):
                if keyboard.is_pressed('e'):
                    ser.write('5')
                    print('pallu is my bae\n')
        else:
            if i > 4:
                ser.write('0')
                i = 0
            i = i+1
            pass
