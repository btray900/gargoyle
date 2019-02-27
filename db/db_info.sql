# osg base db 
DROP DATABASE IF EXISTS osg;
CREATE DATABASE osg;
GRANT SELECT ON osg.* TO 'osg'@'%' IDENTIFIED BY 'xxxFAKEPASSWDxxx';
USE osg;


# CAT from mysqldump start here


