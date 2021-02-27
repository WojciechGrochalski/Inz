#!/bin/bash 
if ${Dotnet} 
then
   echo "Installation packages for dotnet"
   wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
   dpkg -i packages-microsoft-prod.deb
   apt-get update &&
   apt-get install  -y dotnet-sdk-3.1 aspnetcore-runtime-3.1
else echo "No flags dotnet"
fi