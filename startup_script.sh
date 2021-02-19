#!/bin/bash

service mysql start

mysql -uroot <<MYSQL_SCRIPT
CREATE DATABASE phpmyadmin;
CREATE USER 'phpmyadmin'@'localhost' IDENTIFIED BY 'toor';
GRANT ALL PRIVILEGES ON *.*  TO 'phpmyadmin'@'localhost';
FLUSH PRIVILEGES;
select user from mysql.user;
MYSQL_SCRIPT

echo "MySQL user created."
echo "Username:   phpmyadmin"
echo "Password:   phpmyadmin"

sed -i 's/It works!/It works! from Container/g' /var/www/html/index.html


/usr/sbin/apache2ctl -D FOREGROUND  && bash  && service mysql start

