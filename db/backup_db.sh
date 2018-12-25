#!/bin/bash

mv osg.sql osg.sql.backup.old
docker exec -ti db mysqldump --extended-insert=FALSE -u root -pxxxxFAKEPASSWDxxxx osg > mysqldump.sql
cat db_info.sql > osg.sql
cat mysqldump.sql >> osg.sql

