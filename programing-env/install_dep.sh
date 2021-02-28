#!/bin/bash 
if ${Dotnet} 
then
   echo "Installation packages for dotnet"
   pkg=dotnet-sdk-3.1
   status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"
   echo $status
   if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
      echo "package $pkg will be install on background"
   else echo "package $pkg was installed previously"
      dotnet --info
   fi
   
else echo "No flags dotnet"
fi