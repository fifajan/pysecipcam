#! /bin/bash
# can be intergated into crontab.
# be sure that password-less ssh key pair was set up before intergating

HOST="some.internet.host.net"
USER="my_authorized_user"
#PWD="secret"

TIMESTAMP="date +%Y.%m.%d-%Hh.%Mm"

REMOTE_PATH="/path/on/remote/server/projects_and_db_backup.tgz"
STOR_DIR="/stor/backups"

cd $STOR_DIR
echo "Downloading $REMOTE_PATH from $HOST..."
scp $USER@$HOST:$REMOTE_PATH ./projects_and_db_backup_`$TIMESTAMP`.tgz
echo "Done!"
