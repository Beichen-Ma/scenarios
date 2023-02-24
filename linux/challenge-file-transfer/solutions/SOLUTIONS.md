# SOLUTIONS

## Task 1 Solution

```bash
lftp -u root,054422 sftp://192.168.15.128:22<<EOF
get hehe.txt
put haha.txt

```

## Task 2 Solution

```bash
ftp -v -n 192.168.15.128
user qyx 054422
binary
cd /home/qyx/
lcd  /
prompt
put haha.txt
get hehe.txt
bye

```

## Task 3 Solution

```bash

sshpass -p 054422 scp /haha.txt root@192.168.15.128:/root/

```
