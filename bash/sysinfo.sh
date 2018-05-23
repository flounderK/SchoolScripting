#!/bin/bash
#This script will email us our user, IP and hostname.
emailaddress="wolfeco@ucmail.uc.edu"
today=$(date +"%m-%d-%Y")
ip=$(ifconfig | grep 'inet 10' | awk '{print $2}')
printf -v content "User:\t%s\nMy Hostname:\t%s\nMy IP:\t%s\n" $USER $HOSTNAME $ip 
mail -s "IT3030C Linux IP" $emailaddress -r "smtp.uc.edu"<<< $content
