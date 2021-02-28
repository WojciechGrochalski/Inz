#!/bin/bash

echo "start mysql service"
service mysql start
user=phpmyadmin
if [ $(echo "SELECT COUNT(*) FROM mysql.user WHERE user = '$USER'" | mysql | tail -n1) -gt 0 ]
    then
echo "User  exist"
else
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
fi

if ${Dotnet} 
then
   pkg=dotnet-sdk-3.1
   echo $status
   if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
      apt-get install  -y dotnet-sdk-3.1 aspnetcore-runtime-3.1
   else echo "package $pkg was instaled previously"
   fi
   
else echo "No flag dotnet"
fi

echo "start Apache2 service"
sed -i 's/It works!/It works! from Container/g' /var/www/html/index.html
/usr/sbin/apache2ctl -D FOREGROUND 





