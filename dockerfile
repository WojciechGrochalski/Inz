FROM ubuntu:20.04
# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update 

RUN apt install apache2 -y
EXPOSE 80 443
CMD /usr/sbin/apache2ctl -D FOREGROUND