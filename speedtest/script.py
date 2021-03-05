
import os
import time
import speedtest
import json
import socket
try:
    interval = int(os.environ['interval'])
except:
    interval=5
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
def st(ip):
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        res = st.get_best_server()
        print('0) Server location: ',end='')
        print(res["name"])
        print('1) Download Speed: ',end='')
        downloads=round(st.download()/1000000,1)
        print(downloads, "Mbps")
    
        print('1) Upload Speed: ', end='')
        upload=round(st.upload()/1000000,1)
        print(upload, "Mbps")
    
        print('1) Ping: ', end='')
    
        print(st.results.ping)
        data={"downloads":downloads, "uploads": upload, "ping": int(st.results.ping), "ip":ip}
        with open('/var/www/html/speedtest/data.json', 'w') as outfile:
            json.dump(data, outfile)
        
        print("done")
    except Exception as e:
        print(e)
print("Start testing")
ip=get_ip()
while True :
    st(ip)
    time.sleep(interval*60)
print("Exiting program")


