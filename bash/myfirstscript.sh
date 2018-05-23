#!/bin/bash
#This script outputs the IP address and Hostname of a machine
greeting='This is a script. Hello!'
echo "$greeting, thanks for joining us! You owe me \$3"
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME
a=$(ifconfig | grep 'inet 10' | awk '{print $2}')
echo My IP is $a
