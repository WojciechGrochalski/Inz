#!/bin/bash
# pkgs='dotnet-sdk-3.1'
# if dpkg -s $pkgs >/dev/null 2>&1; 
# then
#         dotnet --info   
# fi

#!/bin/bash 
if ${Dotnet} 
then
   pkg=dotnet-sdk-3.1
   status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"
   if [ ! $? = 0 ] || [ ! "$status" = installed ]; then
      echo "package $pkg will be install on background"
   else echo "package $pkg was installed previously"
      dotnet --info
   fi
   
else echo "No flag dotnet"
fi