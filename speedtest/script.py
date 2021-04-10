
import os
import time
import speedtest
import json


try:
    interval = int(os.environ['interval'])
except:
    interval=5

def st():
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
        data={"downloads":downloads, "uploads": upload, "ping": int(st.results.ping)}
        with open('/var/www/localhost/htdocs/speedtest/data.json', 'w') as outfile:
            json.dump(data, outfile)
        
        print("done")
    except Exception as e:
        print(e)
print("Start testing")

while True :
    st()
    time.sleep(interval*60)
print("Exiting program")


