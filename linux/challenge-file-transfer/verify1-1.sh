#!/bin/bash
SFTP_HOST=192.168.15.128
SFTP_PORT="22"
SFTP_PATH="/haha.txt"
SFTP_USER=root
SFTP_PWD=054422
REMOTE_PATH="qyx.txt"

lftp -u ${SFTP_USER},${SFTP_PWD} sftp://${SFTP_HOST}:${PORT}<<EOF
put ${SFTP_PATH}
ls
bye
EOF


