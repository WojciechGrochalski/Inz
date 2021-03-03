import json
import requests
import re
import threading
import time
import RPi.GPIO as GPIO

localGPIOBoard = []
globalGPIOBoard = []
myheaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
end = ""
path = "https://dockerinz.azurewebsites.net/api/Rpi"


def CheckGPIOBoard(localGPIOBoard, globalGPIOBoard):
    for newitem in globalGPIOBoard:
        for item in localGPIOBoard:
            if item.GPIONumber == newitem.GPIONumber:
                if item.GPIOStatus != newitem.GPIOStatus or item.GPIOMode != newitem.GPIOMode:
                    item.GPIOStatus = newitem.GPIOStatus
                    item.GPIOMode = newitem.GPIOMode
                    GPIO.setmode(GPIO.BCM)
                    GPIO.setwarnings(False)
                    if newitem.GPIOMode == "in":
                        GPIO.setup(int(newitem.GPIONumber), GPIO.IN)
                    if newitem.GPIOMode == "out":
                        GPIO.setup(int(newitem.GPIONumber), GPIO.OUT)
                        GPIO.output(int(newitem.GPIONumber), int(newitem.GPIOStatus))


class Gpio:
    def __init__(self, gpioNumber, gpioMode, gpioStatus):
        self.GPIONumber = gpioNumber
        self.GPIOMode = gpioMode
        self.GPIOStatus = gpioStatus


try:
    r = requests.get(path, headers=myheaders)
    dane = json.loads(r.text)
    if len(localGPIOBoard) > 0:
        i = 0
        for value in dane:
            localGPIOBoard[i] = (Gpio(value["gpioNumber"], value["gpioMode"], value["gpioStatus"]))
            i += 1
    else:
        for value in dane:
            localGPIOBoard.append(Gpio(value["gpioNumber"], value["gpioMode"], value["gpioStatus"]))
            localGPIOBoard.sort(key=lambda x: x.GPIONumber)
except:
    print("Nie udało się połączyć z serwerem")


def run():
    time.sleep(5)
    while end != "exit":
        try:
            continousRequest = requests.get(path, headers=myheaders)
            continousdane = json.loads(continousRequest.text)
            if len(globalGPIOBoard) > 0:
                i = 0
                for value in continousdane:
                    globalGPIOBoard[i] = (Gpio(value["gpioNumber"], value["gpioMode"], value["gpioStatus"]))
                    i += 1
            else:
                for value in continousdane:
                    globalGPIOBoard.append(Gpio(value["gpioNumber"], value["gpioMode"], value["gpioStatus"]))
            globalGPIOBoard.sort(key=lambda x: x.GPIONumber)
            CheckGPIOBoard(localGPIOBoard, globalGPIOBoard)
        except Exception as e:
            print(e)
        except:
            print("Nie udało się połączyć z serwerem")
        time.sleep(5)


thread = threading.Thread(target=run, args=())
thread.daemon = True
thread.start()

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
