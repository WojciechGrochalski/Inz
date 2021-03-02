
echo "start Apache2 service"
sed -i 's/It works!/It works! from Container/g' /var/www/html/index.html
# /usr/sbin/apache2ctl -D FOREGROUND && bash
service apache2 start
python script.py

