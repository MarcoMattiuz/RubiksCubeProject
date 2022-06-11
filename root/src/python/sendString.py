import numpy as np
import json
import serial 


class SendString:

    def sendString(string):

        #JSON write    
        # movements ={ "moves":string}
        # with open("../data/data.json","w") as write_file:
        #     json.dump(movements,write_file)

        #Arduino write    
        with  serial.Serial('/dev/cu.usbmodem1201',9600) as ser:
            x = ser.readline()
            print(x)
            x = string+"\n"
            ser.write(x.encode())
            y = ser.readline()
            print(y)
            ser.close()        