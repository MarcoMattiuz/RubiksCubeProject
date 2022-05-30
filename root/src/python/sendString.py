import numpy as np
import json 


class SendString:

    def sendString(string):
        
        movements ={ "moves":string}
        with open("../data/data.json","w") as write_file:
            json.dump(movements,write_file)    