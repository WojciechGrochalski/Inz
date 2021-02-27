#!/bin/bash
pkgs='dotnet-sdk-3.1'
if dpkg -s $pkgs >/dev/null 2>&1; 
then
        dotnet --info   
fi