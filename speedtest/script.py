import os
import time
import speedtest
import json

try:
    interval = int(os.environ['interval'])
except:
    interval = 5




def st():
    downloads = 0.00
    upload = 0.00
    ping = 0
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        res = st.get_best_server()
        print('0) Server location: ', end='')
        print(res["name"])
        data = {"downloads": downloads, "uploads": upload, "ping": int(st.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)
        print('1) Download Speed: ', end='')
        downloads = round(st.download() / 1000000, 1)
        print(downloads, "Mbps")
        data = {"downloads": downloads, "uploads": upload, "ping": int(st.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)
        print('1) Upload Speed: ', end='')
        upload = round(st.upload() / 1000000, 1)
        print(upload, "Mbps")
        print('1) Ping: ', end='')
        print(st.results.ping)
        data = {"downloads": downloads, "uploads": upload, "ping": int(st.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)

        print("done")
    except Exception as e:
        print(e)


print("Start testing")

while True:
    st()
    time.sleep(interval * 60)
print("Exiting program")
