#!/bin/bash
path="/"
file="hehe.txt"
cd $path
history | grep "get" >/dev/null
history=$?
ls -l $file

if (( $? != 0)) && $history
then
        echo "Get failed!"
fi

