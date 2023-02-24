#!/bin/bash
path="/"
file="haha.txt"
sshpass -p "054422" root@192.168.15.128
sleep 3
cd $path
history | grep "put" >/dev/null
history=$?
ls -l $file

if (( $? != 0)) && $history
then
	echo "Pull failed!"
fi
