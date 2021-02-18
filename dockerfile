FROM ubuntu:20.04
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update 
RUN apt-get upgrade -y
RUN apt install -y \
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
      nano


EXPOSE 80 443
RUN echo "Include /etc/phpmyadmin/apache.conf" >>/etc/apache2/apache2.conf
WORKDIR /home
COPY startup_script.py startup_script.py
COPY addUser.sh addUser.sh
RUN python startup_script.py
CMD /usr/sbin/apache2ctl -D FOREGROUND  && bash  




WORKDIR /home
RUN chmod +x addUser.sh 
RUN ./addUser.sh 

RUN echo "service mysql start" >>~/.bashrc
#RUN echo "python /home/addUser.py" >>~/.bashrc

