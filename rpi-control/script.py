import json
import requests
import time
import re
import platform

localGPIOBoard = []
globalGPIOBoard = []
myheaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
end = ""
path = "https://dockerinz.azurewebsites.net/api/Rpi"


class Gpio:
    def __init__(self, gpioNumber, gpioMode, gpioStatus):
        self.GPIONumber = gpioNumber
        self.GPIOMode = gpioMode
        self.GPIOStatus = gpioStatus

while True:
    command = input("$: ")
    if command == 'exit':
        end = "exit"
        break
    parseData = re.findall('\d+', command)
    mode = ""
    if "out" in command:
        mode = "out"
    if "in" in command:
        mode = "in"
    if command.find("out") == -1 and command.find("in") == -1:
        print("Nieznana komenda")
    elif parseData == [] or len(parseData) < 2:
        print("Nieznana komenda")
    else:
        newGpio = Gpio(parseData[0], mode, parseData[1])
        json_string = {"gpioNumber": int(newGpio.GPIONumber),
                       "GPIOStatus": int(newGpio.GPIOStatus),
                       "GPIOMode": newGpio.GPIOMode}
        r = requests.post(path, json=json_string, headers=myheaders)
        if r.status_code == 200:
            print("OK")
        else:
            print("Server not response")
