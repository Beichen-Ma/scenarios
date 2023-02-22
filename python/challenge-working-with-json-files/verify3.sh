#!/bin/zsh
for i in {0..49};
do python json_search.py $i.json $i | grep $i$i
done