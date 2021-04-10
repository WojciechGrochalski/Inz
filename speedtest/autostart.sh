
#!/bin/sh


/usr/sbin/httpd -d FOREGROUND
pip install speedtest-cli -U
python script.py
