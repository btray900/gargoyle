# osg base db - 20181010 - Use mysqldump for table
# bt106c
DROP DATABASE IF EXISTS osg;
CREATE DATABASE osg;
GRANT SELECT ON osg.* TO 'osg'@'%' IDENTIFIED BY 'xxxFAKEPASSWDxxx';
USE osg;

-- MySQL dump 10.16  Distrib 10.3.9-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: osg
-- ------------------------------------------------------
-- Server version	10.3.9-MariaDB-1:10.3.9+maria~bionic

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `securityChecks`
--

DROP TABLE IF EXISTS `securityChecks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `securityChecks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component` varchar(32) NOT NULL,
  `checkID` varchar(32) NOT NULL,
  `checkTask` varchar(64) NOT NULL,
  `command` text NOT NULL,
  `regex` varchar(255) DEFAULT NULL,
  `resource` varchar(255) DEFAULT NULL,
  `expected` varchar(255) DEFAULT NULL,
  `checkValue` varchar(255) DEFAULT NULL,
  `valueLogic` varchar(10) DEFAULT NULL,
  `fkFunction` varchar(64) NOT NULL,
  `info` text DEFAULT NULL,
  `enabled` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=230 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `securityChecks`
--

LOCK TABLES `securityChecks` WRITE;
/*!40000 ALTER TABLE `securityChecks` DISABLE KEYS */;
INSERT INTO `securityChecks` VALUES (8,'keystone','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone','keystone keystone','','','checkFileSystemSecurity','Check directory ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (9,'keystone','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/rootwrap.d','keystone keystone','','','checkFileSystemSecurity','Check directory ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (10,'keystone','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl','keystone keystone','','','checkFileSystemSecurity','Check directory ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (11,'keystone','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl/private','keystone keystone','','','checkFileSystemSecurity','Check directory ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (12,'keystone','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl/certs','keystone keystone','','','checkFileSystemSecurity','Check directory ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (13,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/keystone.conf','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (14,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/keystone-paste.ini','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (15,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/policy.json','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (16,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/logging.conf','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (17,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl/certs/signing_cert.pem','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (18,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl/certs/ca.pem','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (19,'keystone','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','keystone\\skeystone','/etc/keystone/ssl/private/signing_key.pem','keystone keystone','','','checkFileSystemSecurity','Check file ownership on keystone resource',1);
INSERT INTO `securityChecks` VALUES (20,'keystone','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/keystone','750','','','checkFileSystemSecurity','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (21,'keystone','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/keystone/rootwrap.d','750','','','checkFileSystemSecurity','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (22,'keystone','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/keystone/ssl','750','','','checkFileSystemSecurity','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (23,'keystone','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/keystone/ssl/private','750','','','checkFileSystemSecurity','resource info',1);
INSERT INTO `securityChecks` VALUES (24,'keystone','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/keystone/ssl/certs','750','','','checkFileSystemSecurity','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (25,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/keystone.conf','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (26,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/keystone-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (27,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/policy.json','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (28,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/logging.conf','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (29,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/ssl/certs/signing_cert.pem','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (30,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/ssl/certs/ca.pem','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (31,'keystone','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/keystone/ssl/private/signing_key.pem','640','','','checkFileSystemSecurity','Check file permissions on keystone resource',1);
INSERT INTO `securityChecks` VALUES (32,'keystone','03','useTls','/bin/grep -E','^use_tls\\s*=\\s*.*','/etc/keystone/keystone.conf','use_tls = true','true','','checkValueConfigParameter','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (33,'keystone','07','insecureDebug','/bin/grep -E','^insecure_debug\\s*=\\s*.*','/etc/keystone/keystone.conf','insecure_debug = false or commented out','insecure_debug,true','','failIfAllListInLine','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (35,'keystone','06a','disableAdminToken','/bin/grep -E','^admin_token\\s*=\\s*.*','/etc/keystone/keystone.conf','#admin_token = <none>','admin_token','','failIfAllListInLine','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (36,'keystone','06b','disableAdminToken','/bin/grep -E','^AdminTokenAuthMiddleware\\s*.*','/etc/keystone/keystone-paste.ini','#AdminTokenAuthMiddleware','AdminTokenAuthMiddleware','','failIfAllListInLine','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (37,'keystone','05','maxRequestBodySize','/bin/grep -E','^max_request_body_size\\s*=\\s*.*','/etc/keystone/keystone.conf','max_request_body_size = 114688 ###or greater###','114688','gte','checkIntConfigParameter','Check keystone resource',1);
INSERT INTO `securityChecks` VALUES (229,'keystone','08','tokenProvider','/bin/grep -E','^provider\\s*=\\s*.*','/etc/keystone/keystone.conf','provider = fernet','fernet','','checkValueConfigParameter','Check keystone resource.',1);
INSERT INTO `securityChecks` VALUES (39,'cinder','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder','root cinder','','','checkFileSystemSecurity','Check file ownership on cinder resource',1);
INSERT INTO `securityChecks` VALUES (40,'cinder','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder/rootwrap.d','root cinder','','','checkFileSystemSecurity','Check file ownership on cinder resource',1);
INSERT INTO `securityChecks` VALUES (41,'cinder','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder/cinder.conf','root cinder','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (42,'cinder','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder/api-paste.ini','root cinder','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (43,'cinder','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder/policy.json','root cinder','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (44,'cinder','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\scinder','/etc/cinder/rootwrap.conf','root cinder','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (45,'cinder','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/cinder','750','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (46,'cinder','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/cinder/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (47,'cinder','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/cinder/cinder.conf','640','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (48,'cinder','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/cinder/api-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (49,'cinder','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/cinder/policy.json','640','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (50,'cinder','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/cinder/rootwrap.conf','640','','','checkFileSystemSecurity','Check file permissions on cinder resource',1);
INSERT INTO `securityChecks` VALUES (51,'cinder','03','authStrategy','/bin/grep -E','^auth_strategy\\s*=\\s*.*','/etc/cinder/cinder.conf','auth_strategy = keystone','keystone','','checkValueConfigParameter','Check auth strategy for cinder resource',1);
INSERT INTO `securityChecks` VALUES (52,'cinder','04a','authURI','/bin/grep -E','^auth_uri\\s*=\\s*.*','/etc/cinder/cinder.conf','auth_uri = https://[identity-api]','https','','checkValueConfigParameter','Check auth URI for cinder resource',1);
INSERT INTO `securityChecks` VALUES (53,'cinder','04b','secureAuthProtocol','/bin/grep -E','^insecure\\s*=\\s*.*','/etc/cinder/cinder.conf','insecure = false','false','','checkValueConfigParameter','Check secure auth protocol on cinder resource',1);
INSERT INTO `securityChecks` VALUES (54,'cinder','05','novaApiInsecure','/bin/grep -E','^nova_api_insecure\\s*=\\s*.*','/etc/cinder/cinder.conf','nova_api_insecure = false','false','','checkValueConfigParameter','Check nova api secure on cinder resource',1);
INSERT INTO `securityChecks` VALUES (55,'cinder','06a','glanceApiInsecure','/bin/grep -E','^glance_api_insecure\\s*=\\s*.*','/etc/cinder/cinder.conf','glance_api_insecure = false','false','','checkValueConfigParameter','Check glance api insecure on cinder resource',1);
INSERT INTO `securityChecks` VALUES (56,'cinder','06b','glanceApiServers','/bin/grep -E','^glance_api_servers\\s*=\\s*.*','/etc/cinder/cinder.conf','glance_api_servers = https://[glance_api]','https','','checkValueConfigParameter','Check glance API servers on cinder resource',1);
INSERT INTO `securityChecks` VALUES (57,'cinder','08a','osapiMaxRequestBodySize','/bin/grep -E','^osapi_max_request_body_size\\s*=\\s*.*','/etc/cinder/cinder.conf','osapi_max_request_body_size = 114688 ###or greater###','114688','gte','checkIntConfigParameter','Check osapi max request body size on cinder resource',1);
INSERT INTO `securityChecks` VALUES (58,'cinder','08b','maxRequestBodySize','/bin/grep -E','^max_request_body_size\\s*=\\s*.*','/etc/cinder/cinder.conf','max_request_body_size = 114688 ###or greater###','114688','gte','checkIntConfigParameter','Check max request body size on cinder resource',1);
INSERT INTO `securityChecks` VALUES (59,'glance','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (60,'glance','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/rootwrap.d','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (61,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-api.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (62,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-api-paste.ini','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (63,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-cache.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (64,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-manage.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (65,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-registry-paste.ini','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (66,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-registry.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (67,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-scrubber.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (68,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/glance-swift-store.conf','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (69,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/policy.json','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (70,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/schema-image.json','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (71,'glance','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sglance','/etc/glance/schema.json','root glance','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (72,'glance','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/glance','750','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (73,'glance','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/glance/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (74,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-api.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (75,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-api-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (76,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-cache.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (77,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-manage.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (78,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-registry-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (79,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-registry.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (80,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-scrubber.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (81,'glance','01','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/glance-swift-store.conf','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (82,'glance','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/policy.json','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (83,'glance','01','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/schema-image.json','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (84,'glance','01','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/glance/schema.json','640','','','checkFileSystemSecurity','Check file permissions on glance resource',1);
INSERT INTO `securityChecks` VALUES (85,'glance','03','authStrategy','/bin/grep -E','^auth_strategy\\s*=\\s*.*','/etc/glance/glance-api.conf','auth_strategy = keystone','keystone','','checkValueConfigParameter','Check auth strategy for glance resource',1);
INSERT INTO `securityChecks` VALUES (86,'glance','04a','authURI','/bin/grep -E','^auth_uri\\s*=\\s*.*','/etc/glance/glance-api.conf','auth_uri = https://[identity-api]','https','','checkValueConfigParameter','Check auth URI for glance resource',1);
INSERT INTO `securityChecks` VALUES (87,'glance','04b','secureAuthProtocol','/bin/grep -E','^insecure\\s*=\\s*.*','/etc/glance/glance-api.conf','insecure = false','false','','checkValueConfigParameter','Check secure auth protocol on glance resource',1);
INSERT INTO `securityChecks` VALUES (88,'glance','05','protectCopyFrom','/bin/grep -E','.*copy_from.*','/etc/glance/policy.json','\"copy_from\": \"rule: admin_create\"','admin_create','','checkSubstrConfigParameter','Check restricted copy_from directive on glance resource',1);
INSERT INTO `securityChecks` VALUES (89,'heat','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (90,'heat','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat/rootwrap.d','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (91,'heat','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat/heat.conf','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (92,'heat','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat/api-paste.ini','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (93,'heat','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat/policy.json','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (94,'heat','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sheat','/etc/heat/rootwrap.conf','root heat','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (95,'heat','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/heat','750','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (96,'heat','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/heat/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (97,'heat','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/heat/heat.conf','640','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (98,'heat','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/heat/api-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (99,'heat','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/heat/policy.json','640','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (100,'heat','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/heat/rootwrap.conf','640','','','checkFileSystemSecurity','Check file permissions on heat resource',1);
INSERT INTO `securityChecks` VALUES (101,'horizon','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\shorizon','/etc/openstack-dashboard','root horizon','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (102,'horizon','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\shorizon','/etc/openstack-dashboard/rootwrap.d','root horizon','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (103,'horizon','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\shorizon','/etc/openstack-dashboard/local_settings.py','root horizon','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (104,'horizon','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/openstack-dashboard','750','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (105,'horizon','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/openstack-dashboard/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (106,'horizon','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/openstack-dashboard/local_settings.py','640','','','checkFileSystemSecurity','Check file permissions on horizon resource',1);
INSERT INTO `securityChecks` VALUES (107,'horizon','03','disallowIframeEmbed','/bin/grep -E','^DISALLOW_IFRAME_EMBED\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','DISALLOW_IFRAME_EMBED = True','true','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (108,'horizon','04','csrfCookieSecure','/bin/grep -E','^CSRF_COOKIE_SECURE\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','CSRF_COOKIE_SECURE = True','true','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (109,'horizon','05','sessionCookieSecure','/bin/grep -E','^SESSION_COOKIE_SECURE\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','SESSION_COOKIE_SECURE = True','true','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (110,'horizon','06','sessionCookieHttponly','/bin/grep -E','^SESSION_COOKIE_HTTPONLY\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','SESSION_COOKIE_HTTPONLY = True','true','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (111,'horizon','07','passwordAutocomplete','/bin/grep -E','^PASSWORD_AUTOCOMPLETE\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','PASSWORD_AUTOCOMPLETE = False','false','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (112,'horizon','08','disablePasswordReveal','/bin/grep -E','^DISABLE_PASSWORD_REVEAL\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','DISABLE_PASSWORD_REVEAL = True','true','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (113,'horizon','09','enforePasswordCheck','/bin/grep -E','^ENFORCE_PASSWORD_CHECK\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','ENFORCE_PASSWORD_CHECK = True','true','','checkValueConfigParameter','Check setting for horizon resource.',1);
INSERT INTO `securityChecks` VALUES (114,'horizon','11','secureProxySslHeader','/bin/grep -E','^SECURE_PROXY_SSL_HEADER\\s*=\\s*.*','/etc/openstack-dashboard/local_settings.py','SECURE_PROXY_SSL_HEADER = (\'HTTP_X_FORWARDED_PROTOCOL\', \'https\')','https','','checkValueConfigParameter','Check setting for horizon resource',1);
INSERT INTO `securityChecks` VALUES (121,'neutron','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (122,'neutron','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron/rootwrap.d','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (123,'neutron','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron/neutron.conf','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (124,'neutron','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron/api-paste.ini','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (125,'neutron','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron/policy.json','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (126,'neutron','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sneutron','/etc/neutron/rootwrap.conf','root neutron','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (127,'neutron','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/neutron','750','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (128,'neutron','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/neutron/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (129,'neutron','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/neutron/neutron.conf','640','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (130,'neutron','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/neutron/api-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (131,'neutron','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/neutron/policy.json','640','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (132,'neutron','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/neutron/rootwrap.conf','640','','','checkFileSystemSecurity','Check file permissions on neutron resource',1);
INSERT INTO `securityChecks` VALUES (133,'neutron','03','authStrategy','/bin/grep -E','^auth_strategy\\s*=\\s*.*','/etc/neutron/neutron.conf','auth_strategy = keystone','keystone','','checkValueConfigParameter','Check auth strategy for neutron resource',1);
INSERT INTO `securityChecks` VALUES (134,'neutron','04a','authURI','/bin/grep -E','^auth_uri\\s*=\\s*.*','/etc/neutron/neutron.conf','auth_uri = https://[identity-api]','https','','checkValueConfigParameter','Check auth URI for neutron resource',1);
INSERT INTO `securityChecks` VALUES (135,'neutron','04b','secureAuthProtocol','/bin/grep -E','^insecure\\s*=\\s*.*','/etc/neutron/neutron.conf','insecure = false','false','','checkValueConfigParameter','Check secure auth protocol on neutron resource',1);
INSERT INTO `securityChecks` VALUES (136,'neutron','05','useSsl','/bin/grep -E','^use_ssl\\s*=\\s*.*','/etc/neutron/neutron.conf','use_ssl = true','true','','checkValueConfigParameter','Check nova api secure on neutron resource',1);
INSERT INTO `securityChecks` VALUES (137,'neutron','ap','authProtocol','/bin/grep -E','^auth_protocol\\s*=\\s*.*','/etc/neutron/neutron.conf','auth_protocol = https','https','','checkValueConfigParameter','Check auth protocol on neutron resource',1);
INSERT INTO `securityChecks` VALUES (138,'nova','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (139,'nova','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova/rootwrap.d','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (140,'nova','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova/nova.conf','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (141,'nova','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova/api-paste.ini','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (142,'nova','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova/policy.json','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (143,'nova','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\snova','/etc/nova/rootwrap.conf','root nova','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (144,'nova','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/nova','750','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (145,'nova','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/nova/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (146,'nova','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/nova/nova.conf','640','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (147,'nova','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/nova/api-paste.ini','640','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (148,'nova','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/nova/policy.json','640','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (149,'nova','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/nova/rootwrap.conf','640','','','checkFileSystemSecurity','Check file permissions on nova resource',1);
INSERT INTO `securityChecks` VALUES (150,'nova','03','authStrategy','/bin/grep -E','^auth_strategy\\s*=\\s*.*','/etc/nova/nova.conf','auth_strategy = keystone','keystone','','checkValueConfigParameter','Check auth strategy for nova resource',1);
INSERT INTO `securityChecks` VALUES (151,'nova','04a','authURI','/bin/grep -E','^auth_uri\\s*=\\s*.*','/etc/nova/nova.conf','auth_uri = https://[identity-api]','https','','checkValueConfigParameter','Check auth URI for nova resource',1);
INSERT INTO `securityChecks` VALUES (152,'nova','04b','secureAuthProtocol','/bin/grep -E','^insecure\\s*=\\s*.*','/etc/nova/nova.conf','insecure = false','false','','checkValueConfigParameter','Check secure auth protocol on nova resource',1);
INSERT INTO `securityChecks` VALUES (153,'nova','05a','apiInsecure','/bin/grep -E','^api_insecure\\s*=\\s*.*','/etc/nova/nova.conf','api_insecure = false','false','','checkValueConfigParameter','Check nova api secure on nova resource',1);
INSERT INTO `securityChecks` VALUES (154,'nova','05b','apiServers','/bin/grep -E','^api_servers\\s*=\\s*.*','/etc/nova/nova.conf','api_servers = https://[image-api]','https','','checkValueConfigParameter','Check nova api secure on nova resource',1);
INSERT INTO `securityChecks` VALUES (155,'swift','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (156,'swift','00','directoryOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/rootwrap.d','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (157,'swift','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/account.builder','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (159,'swift','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/container.builder','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (162,'swift','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/object.builder','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (164,'swift','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/proxy-server.conf','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (165,'swift','01','fileOwnership','/usr/bin/stat -L -c \\\"%U %G\\\"','root\\sswift','/etc/swift/swift.conf','root swift','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (166,'swift','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/swift','750','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (167,'swift','00','directoryPermissions','/usr/bin/stat -L -c \\\"%a\\\"','750','/etc/swift/rootwrap.d','750','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (168,'swift','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/swift/account.builder','640','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (170,'swift','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/swift/container.builder','640','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (173,'swift','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/swift/object.builder','640','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (175,'swift','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/swift/proxy-server.conf','640','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (176,'swift','02','filePermissions','/usr/bin/stat -L -c \\\"%a\\\"','640','/etc/swift/swift.conf','640','','','checkFileSystemSecurity','Check file permissions on swift resource',1);
INSERT INTO `securityChecks` VALUES (177,'swift','ap','authProtocol','/bin/grep -E','^auth_protocol\\s*=\\s*.*','/etc/swift/proxy-server.conf','auth_protocol = https','https','','checkValueConfigParameter','Check auth protocol on swift resource',1);
INSERT INTO `securityChecks` VALUES (178,'swift','03','authStrategy','/bin/grep -E','^auth_strategy\\s*=\\s*.*','/etc/swift/swift.conf','auth_strategy = keystone','keystone','','checkValueConfigParameter','Check auth strategy for swift resource',1);
