#! /bin/bash

# this script requires lftp package, NAS (network attached storage)
# accessable by FTP protocol (user should have write perms)

NAS_IP="128.64.32.16" # domain/host name should work too 
NAS_AUTH="user_name:user_pwd"
FTP_N_OPTS="lftp -e"

TAR_NAME="projects_backup.tgz"
TIMESTAMP="date +%Y.%m.%d-%Hh.%Mm"
TAR_DATE_NAME="projects_backup_`$TIMESTAMP`.tgz"

REMOTE_CMD="open ftp://$NAS_AUTH@$NAS_IP/backups ; mput $TAR_NAME ; \
            mv $TAR_NAME $TAR_DATE_NAME ; exit ;"

SERV_BACKUP_DIR="/home/user/backups"


cd $SERV_BACKUP_DIR

$FTP_N_OPTS "$REMOTE_CMD"
