
FROM ubuntu:20.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

#Instalation packages
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y \
    apt-utils \
      apache2 \
      mysql-server \
      mysql-client \
      phpmyadmin \
      php-mbstring \
      php-zip \
      php-gd \
      php-json \
      php-curl \
      python-dev \
      nano \
      wget \
      apt-transport-https \
      wget

#Instalation dotnet
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update 
RUN apt-get install -y \
      dotnet-sdk-3.1 \
      aspnetcore-runtime-3.1

#Config Apache server
EXPOSE 80 443
RUN echo "Include /etc/phpmyadmin/apache.conf" >>/etc/apache2/apache2.conf
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

#Adding Scripts
WORKDIR /home
COPY startup_script.sh startup_script.sh
RUN chmod +x startup_script.sh
COPY dotnet.sh dotnet.sh
RUN chmod +x dotnet.sh
RUN usermod -d /var/lib/mysql/ mysql
WORKDIR /etc/phpmyadmin
RUN rm config-db.php
COPY config-db.php  config-db.php
WORKDIR /home
RUN echo "/home/dotnet.sh" >>~/.bashrc

#Run services on start container
CMD ./startup_script.sh 


