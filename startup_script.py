import os

# file = open('/etc/apache2/apache2.conf', 'a')
# file.write('Include /etc/phpmyadmin/apache.conf')
# file.close()
os.system("usermod -d /var/lib/mysql/ mysql")
#os.system("service apache2 start && service mysql start ")