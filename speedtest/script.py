
import os
import re
import subprocess
import time
import speedtest
import threading
import json
#def run():

print("Start testing")

while True :
    #os.system(f"sed -i 's/Configuration Overview/start/g' /var/www/html/speedtest/index.html")
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
    with open('/var/www/html/speedtest/data.json', 'w') as outfile:
        json.dump(data, outfile)
    exit=input('$:')
    if(exit=='exit'):
        break
print("Exiting program")

# thread = threading.Thread(target=run, args=())
# thread.daemon = True
# thread.start()

#   Html_file= open("/var/www/html/speedtest/index.html","r")
#     html_str=Html_file.read()
#     Html_file.close()
#     html_str = html_str.replace(html, "<div id=""dlText"" class=""meterText"">{downloads}</div>")
 
#     Html_file= open("/var/www/html/speedtest/index.html","w")
#     Html_file.write(html_str)
#     Html_file.close()