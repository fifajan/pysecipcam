#! /bin/bash

PRIORITY="nice -19" # low
ZIP_LEVEL="-9" # high ratio compression

cd /backups/directory/

echo 'Backup packing:'
echo 'PG bases dumping...' # PG = PostgreSQL
$PRIORITY pg_dumpall > /home/web/projects/vps_pg_dbs_all.sql
echo 'Done!   Projects packing...'
GZIP=$ZIP_LEVEL $PRIORITY tar -cvzf projects_and_db_backup.tgz /path/to/projects/root/dir
echo 'All done!   TO DOWNLOAD: $ scp user@host:/path/to/backup.tgz .'
