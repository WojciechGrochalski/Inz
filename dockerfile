FROM ubuntu:20.04
LABEL maintainer: Wojciech Grochalski

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive
ARG Dotnet=false
ENV Dotnet ${Dotnet}
#Installation packages
LABEL Installation packages
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

#Installation dotnet
 LABEL Installation packages
 WORKDIR /home
 COPY install_dep.sh install_dep.sh
 RUN chmod +x install_dep.sh
 RUN ./install_dep.sh
# RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
# RUN dpkg -i packages-microsoft-prod.deb
# RUN apt-get update 
# RUN apt-get install -y \
#       dotnet-sdk-3.1 \
#       aspnetcore-runtime-3.1

#Config Apache server
LABEL Config Apache server
EXPOSE 80 443
RUN echo "Include /etc/phpmyadmin/apache.conf" >>/etc/apache2/apache2.conf
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

#Adding Scripts
LABEL Adding Scripts
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

#Run services on startup container
LABEL Run services on startup container
CMD ./startup_script.sh 


