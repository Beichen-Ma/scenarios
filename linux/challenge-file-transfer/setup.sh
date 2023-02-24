#!/bin/bash
package="vsftpd-3.0.2-25.el7.x86_64.rpm"
packageName="vsftpd"
apt-get install rpm
search=$( rpm -qa | grep "${packageName}" )

if (( $? != 0))
then
	rpm -i ${package}
fi
sleep 3

systemctl stop firewalld

username="qyx"
password="054422"
remote_path="/home/qyx"
ip="192.168.15.128"
local_path="/"
put_file="haha.txt"
get_file="hehe.txt"

ftp -v -n $ip<<EOF
user $username $password
binary
cd $remote_path
lcd  $local_path
prompt
put $put_file
get $get_file
bye
EOF
