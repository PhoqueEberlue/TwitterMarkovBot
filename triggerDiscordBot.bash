#!/bin/bash

### Set initial time of file
LTIME=`stat -c %Z ~/TwitterMarkovBot/logs.json`

while true
do
   ATIME=`stat -c %Z ~/TwitterMarkovBot/logs.json`

   if [[ "$ATIME" != "$LTIME" ]]
   then
       python3 ~/TwitterMarkovBot/discordBot.py
       LTIME=$ATIME
   fi
   sleep 5
done
