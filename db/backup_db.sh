#!/bin/bash

mv osg.sql osg.sql.backup.old
docker exec -ti db mysqldump --extended-insert=FALSE -u ${DB_ROOT_USER} -p${DB_ROOT_PW} ${DB_DATABASE} > mysqldump.sql
cat db_info.sql > osg.sql
cat mysqldump.sql >> osg.sql

