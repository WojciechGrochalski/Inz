import platform
import os

if platform.machine()=="armv7l":
     print("You used RPI!")
     os.system("python3 scriptRPI.py")
else:
    print("You dont use RPI!")
    os.system("python3 script.py")