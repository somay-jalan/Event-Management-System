-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: DBMS_Project_final
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `AID` int unsigned NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL,
  `Approved` set('YES','NO','REJECTED') NOT NULL DEFAULT 'NO',
  PRIMARY KEY (`AID`),
  UNIQUE KEY `AID_UNIQUE` (`AID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  CONSTRAINT `atRateCheck` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `check_name_length` CHECK ((char_length(`Name`) > 2)),
  CONSTRAINT `checkpasswordlength` CHECK ((char_length(`Password`) > 7)),
  CONSTRAINT `checkPhoneNoLength` CHECK ((char_length(`PhoneNo`) >= 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Admin1','admin1@example.com','admin123','1234567890','YES'),(2,'Admin2','admin2@example.com','securepass','9876543210','NO'),(3,'Admin3','admin3@example.com','password123','1112223333','NO'),(4,'Admin4','admin4@example.com','adminpass','5556667777','NO'),(5,'Admin5','admin5@example.com','strongpassword','9998887777','NO'),(11511110,'somay','somay@gmail.com','12345678','1234567890','YES');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `EID` int unsigned NOT NULL,
  `StartDateTime` datetime NOT NULL,
  `EndDateTime` datetime NOT NULL,
  `Description` varchar(300) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `NumberOfParticipants` int unsigned NOT NULL,
  `Type` set('Free','Ticketed') NOT NULL,
  `RequirementsForParticipants` json DEFAULT NULL,
  `OID` int unsigned NOT NULL,
  `Approved` set('NO','YES','REJECTED') NOT NULL DEFAULT 'NO',
  `max_participants` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`EID`),
  UNIQUE KEY `EID_UNIQUE` (`EID`),
  KEY `fk_events_OID` (`OID`),
  CONSTRAINT `fk_events_OID` FOREIGN KEY (`OID`) REFERENCES `organizer` (`OID`),
  CONSTRAINT `checkname_length` CHECK ((char_length(`name`) > 2))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'2022-03-01 10:00:00','2022-03-01 12:00:00','Enjoy the research event','RIISE',100,'Free','{\"qualification\": \"NA\"}',1,'YES',0),(2,'2022-03-02 11:00:00','2022-03-02 13:00:00','Workshop on Data Science','DataWorks',50,'Ticketed','{\"qualification\": \"Intermediate\"}',2,'NO',0),(3,'2022-03-03 14:00:00','2022-03-03 16:00:00','Art Exhibition','ArtisticVisions',75,'Free','{\"qualification\": \"NA\"}',3,'YES',0),(4,'2022-03-04 09:30:00','2022-03-04 11:30:00','Tech Summit','TechPulse',120,'Ticketed','{\"experience\": \"Advanced\"}',1,'NO',0),(5,'2022-03-05 15:30:00','2022-03-05 17:30:00','Fitness Challenge','FitLife',80,'Free','{\"qualification\": \"NA\"}',2,'NO',0),(6,'2022-03-06 12:00:00','2022-03-06 14:00:00','Book Fair','BookWorms',200,'Free','{\"qualification\": \"NA\"}',3,'NO',0),(7,'2022-03-07 13:45:00','2022-03-07 15:45:00','Coding Bootcamp','CodeMasters',60,'Ticketed','{\"technology\": \"Java\"}',1,'NO',0),(8,'2022-03-08 17:00:00','2022-03-08 19:00:00','Cooking Class','CulinaryDelights',40,'Ticketed','{\"cuisine\": \"Italian\"}',2,'NO',0),(9,'2022-03-09 09:00:00','2022-03-09 11:00:00','Environmental Cleanup','EcoWarriors',150,'Free','{\"qualification\": \"NA\"}',3,'NO',0),(10,'2022-03-10 16:30:00','2022-03-10 18:30:00','Photography Workshop','PhotoPros',70,'Ticketed','{\"equipment\": \"DSLR\"}',1,'NO',0),(11,'2022-03-11 14:30:00','2022-03-11 16:30:00','Chess Tournament','StrategicMoves',50,'Free','{\"qualification\": \"NA\"}',2,'YES',0),(12,'2022-03-12 11:15:00','2022-03-12 13:15:00','Networking Mixer','ConnectNow',90,'Free','{\"qualification\": \"NA\"}',3,'YES',0),(13,'2022-03-13 18:00:00','2022-03-13 20:00:00','Film Screening','CinephilesClub',120,'Ticketed','{\"genre\": \"Drama\"}',1,'YES',0),(14,'2022-03-14 12:45:00','2022-03-14 14:45:00','Gardening Workshop','GreenThumb',40,'Free','{\"qualification\": \"NA\"}',2,'YES',0),(15,'2022-03-15 10:45:00','2022-03-15 12:45:00','DIY Craft Fair','CraftyCreations',80,'Free','{\"qualification\": \"NA\"}',3,'YES',0),(16,'2022-03-16 16:15:00','2022-03-16 18:15:00','Language Exchange','LingoLovers',30,'Ticketed','{\"languages\": [\"French\", \"Spanish\"]}',1,'NO',0),(17,'2022-03-17 13:30:00','2022-03-17 15:30:00','Music Festival','HarmonyFest',200,'Free','{\"qualification\": \"NA\"}',2,'NO',0),(18,'2022-03-18 09:15:00','2022-03-18 11:15:00','Virtual Reality Demo','VRZone',50,'Ticketed','{\"experience\": \"Beginner\"}',3,'YES',0),(19,'2022-03-19 14:00:00','2022-03-19 16:00:00','Science Fair','SciTechExpo',100,'Free','{\"qualification\": \"NA\"}',1,'NO',0),(20,'2022-03-20 15:30:00','2022-03-20 17:30:00','Music Concert','MelodyMasters',200,'Free','{\"qualification\": \"NA\"}',3,'YES',0),(21,'2024-05-01 10:00:00','2024-05-02 12:00:00','Computer Hackathon','IEEE',1,'Free','{\"qualification\": \"NA\"}',1,'YES',1),(10211112,'2024-12-12 00:00:00','2024-12-12 00:00:00','ssasasa','sassaa',0,'Free','null',1,'NO',0),(10211113,'2024-12-12 00:00:00','2024-12-12 00:00:00','saaassaa','assasa',0,'Free','{\"\": \"\"}',1,'NO',0),(10211114,'2022-12-12 00:00:00','2022-12-12 00:00:00','sddsdsdsdsds','ssdsds',0,'Free','{\"5\": \"4\"}',1,'NO',0),(10211115,'2024-12-12 00:00:00','2024-12-14 00:00:00','asaasaggfg','sass',0,'Free','null',1,'NO',0),(11511111,'2024-05-12 00:00:00','2024-05-14 00:00:00','hacky','ACMM',1,'Ticketed','{\"hard\": \"yes\"}',11511110,'YES',0),(11511112,'2022-12-20 00:00:00','2022-12-22 00:00:00','pasttt','pastevent',0,'Free','null',11511110,'NO',0),(11511113,'2022-12-12 00:00:00','2022-12-14 00:00:00','hackathon','ieee',0,'Free','null',11511110,'NO',1);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`somay`@`localhost`*/ /*!50003 TRIGGER `events_BEFORE_INSERT` BEFORE INSERT ON `events` FOR EACH ROW BEGIN
DECLARE unapproved_events_count INT;
    
    
    SELECT COUNT(*) INTO unapproved_events_count FROM events WHERE OID = NEW.OID AND approved = 'NO';
    
    IF unapproved_events_count >= 5 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Organizer already has 5 or more unapproved events!';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `organizer`
--

DROP TABLE IF EXISTS `organizer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organizer` (
  `OID` int unsigned NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Club/Seminar` varchar(30) NOT NULL,
  `Approved` set('YES','NO','REJECTED') NOT NULL DEFAULT 'NO',
  PRIMARY KEY (`OID`),
  UNIQUE KEY `OID_UNIQUE` (`OID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  CONSTRAINT `check_namelength` CHECK ((char_length(`Name`) > 2)),
  CONSTRAINT `emailCheck` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `password_length` CHECK ((char_length(`Password`) > 7))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizer`
--

LOCK TABLES `organizer` WRITE;
/*!40000 ALTER TABLE `organizer` DISABLE KEYS */;
INSERT INTO `organizer` VALUES (1,'Foobar','foobar@example.com','foobarpass','Club','YES'),(2,'65th Square','65thsquare@example.com','squarepass','Club','YES'),(3,'Electroholics','electroholics@example.com','electropass','Club','YES'),(4,'Salt and Pepper','saltandpepper@example.com','saltnpepperpass','Club','NO'),(5,'Riise','riise@example.com','riisepass','Seminar','NO'),(6,'Tech Wizards','techwizards@example.com','techpass','Club','YES'),(7,'Innovation Hub','innovationhub@example.com','innovationpass','Club','YES'),(8,'Creative Minds','creativeminds@example.com','creativepass','Club','NO'),(9,'Science Explorers','scienceexplorers@example.com','sciencepass','Club','NO'),(10,'Art Enthusiasts','artenthusiasts@example.com','artapass','Club','NO'),(11511110,'somay','somay@gmail.com','123456789','Club','YES');
/*!40000 ALTER TABLE `organizer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participant`
--

DROP TABLE IF EXISTS `participant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participant` (
  `PID` int unsigned NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Password` varchar(45) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL,
  `RollNo` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`PID`),
  UNIQUE KEY `PID_UNIQUE` (`PID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  CONSTRAINT `checknamelength` CHECK ((char_length(`name`) > 2)),
  CONSTRAINT `checkphonelength` CHECK ((char_length(`PhoneNo`) >= 10)),
  CONSTRAINT `emailatRateCheck` CHECK ((`Email` like _utf8mb4'%@%.%')),
  CONSTRAINT `passwordlength` CHECK ((char_length(`Password`) > 7))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participant`
--

LOCK TABLES `participant` WRITE;
/*!40000 ALTER TABLE `participant` DISABLE KEYS */;
INSERT INTO `participant` VALUES (1,'Rahul Sharma','rahulsharma@example.com','12345678','7533205503','2022450'),(2,'Priya Kapoor','priyakapoor@example.com','password2','9876543210','2022451'),(3,'Ravi Singh','ravsingh@example.com','password3','1112223333','2022452'),(4,'Ananya Patel','ananyapatel@example.com','password4','9998887777','2022453'),(5,'Vikram Joshi','vikramjoshi@example.com','password5','8887776666','2022454'),(6,'Ayesha Gupta','ayeshagupta@example.com','password6','7776665555','2022455'),(7,'Rajni Kumar','rajnikumar@example.com','password7','6665554444','2022456'),(8,'Harish Malhotra','harishmalhotra@example.com','password8','5554443333','2022457'),(9,'Meera Sharma','meerasharma@example.com','password9','4443332222','2022458'),(10,'Arjun Kapoor','arjunkapoor@example.com','password10','3332221111','2022459'),(11,'Neha Verma','nehaverma@example.com','password11','2221110000','2022460'),(12,'Karan Singh','karansingh@example.com','password12','1110009999','2022461'),(13,'Pooja Sharma','poojasharma@example.com','password13','0009998888','2022462'),(14,'Amit Gupta','amitgupta@example.com','password14','8888777777','2022463'),(15,'Simran Kaur','simrankaur@example.com','password15','7777666666','2022464'),(16,'Vishal Joshi','vishaljoshi@example.com','password16','6666555555','2022465'),(17,'Sonia Kapoor','soniakapoor@example.com','password17','5555444444','2022466'),(18,'Rahul Verma','rahulverma@example.com','password18','4444333333','2022467'),(19,'Divya Sharma','divyasharma@example.com','password19','3333222222','2022468'),(20,'Alok Singh','aloksingh@example.com','password20','2222111111','2022469'),(21,'Mona Malhotra','monamalhotra@example.com','password21','1111000000','2022470'),(22,'Rajat Gupta','rajatgupta@example.com','password22','0000999999','2022471'),(23,'Sanya Verma','sanyaverma@example.com','password23','9999888888','2022472'),(24,'Amit Sharma','amitsharma@example.com','password24','8888777777','2022473'),(25,'Anjali Singh','anjalisingh@example.com','password25','7777666666','2022474'),(26,'Rohan Kapoor','rohankapoor@example.com','password26','6666555555','2022475'),(27,'Neha Joshi','nehajoshi@example.com','password27','5555444444','2022476'),(28,'Vivek Sharma','viveksharma@example.com','password28','4444333333','2022477'),(29,'Riya Verma','riyaverma@example.com','password29','3333222222','2022478'),(30,'Kunal Singh','kunalsingh@example.com','password30','2222111111','2022479'),(31,'Preeti Malhotra','preetimalhotra@example.com','password31','1111000000','2022480'),(32,'Rohit Gupta','rohitgupta@example.com','password32','0000999999','2022481'),(33,'Sonam Verma','sonamverma@example.com','password33','9999888888','2022482'),(34,'Rahul Sharma','rahulsharma2@example.com','password34','8888777777','2022483'),(35,'Aarti Singh','aartisingh@example.com','password35','7777666666','2022484'),(36,'Vikas Kapoor','vikaskapoor@example.com','password36','6666555555','2022485'),(37,'Juhi Joshi','juhijoshi@example.com','password37','5555444444','2022486'),(38,'Alok Verma','alokverma@example.com','password38','4444333333','2022487'),(39,'Ishita Sharma','ishitasharma@example.com','password39','3333222222','2022488'),(40,'Raj Singh','rajsingh@example.com','password40','2222111111','2022489'),(41,'Kirti Malhotra','kirtimalhotra@example.com','password41','1111000000','2022490'),(42,'Ravi Gupta','ravigupta@example.com','password42','0000999999','2022491'),(43,'Sapna Verma','sapnaverma@example.com','password43','9999888888','2022492'),(44,'Rajat Sharma','rajatsharma@example.com','password44','8888777777','2022493'),(45,'Anita Singh','anitasingh@example.com','password45','7777666666','2022494'),(46,'Vishal Kapoor','vishalkapoor@example.com','password46','6666555555','2022495'),(47,'Pooja Joshi','poojajoshi@example.com','password47','5555444444','2022496'),(48,'Amit Verma','amitverma@example.com','password48','4444333333','2022497'),(49,'Simran Sharma','simransharma@example.com','password49','3333222222','2022498'),(50,'Divya Verma','divyaverma@example.com','password50','1112223333','2022499'),(11511110,'somay','somay@gmail.com','1234567890','1234567890',NULL),(11511111,'somay','somay2@gmail.com','123456789','1234567890',NULL),(11511112,'somay','somay@example.com','12345678','12345456789','2021'),(99111109,'somay','somay1@gmail.com','1234567890','1234567890',NULL);
/*!40000 ALTER TABLE `participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `participant_events`
--

DROP TABLE IF EXISTS `participant_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participant_events` (
  `PID` int unsigned NOT NULL,
  `EID` int unsigned NOT NULL,
  PRIMARY KEY (`PID`,`EID`),
  KEY `EID` (`EID`),
  CONSTRAINT `participant_events_ibfk_1` FOREIGN KEY (`PID`) REFERENCES `participant` (`PID`),
  CONSTRAINT `participant_events_ibfk_2` FOREIGN KEY (`EID`) REFERENCES `events` (`EID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participant_events`
--

LOCK TABLES `participant_events` WRITE;
/*!40000 ALTER TABLE `participant_events` DISABLE KEYS */;
INSERT INTO `participant_events` VALUES (1,1),(3,1),(5,1),(7,1),(49,1),(1,2),(3,2),(5,2),(7,2),(49,2),(1,3),(3,3),(5,3),(7,3),(49,3),(1,4),(3,4),(5,4),(7,4),(49,4),(1,5),(3,5),(5,5),(7,5),(49,5),(2,6),(4,6),(6,6),(8,6),(50,6),(2,7),(4,7),(6,7),(8,7),(50,7),(2,8),(4,8),(6,8),(8,8),(50,8),(2,9),(4,9),(6,9),(8,9),(50,9),(2,10),(4,10),(6,10),(8,10),(50,10),(1,11),(3,11),(5,11),(7,11),(9,11),(1,12),(3,12),(5,12),(7,12),(9,12),(1,13),(3,13),(5,13),(7,13),(9,13),(1,14),(3,14),(5,14),(7,14),(9,14),(1,15),(3,15),(5,15),(7,15),(9,15),(2,16),(4,16),(6,16),(8,16),(10,16),(2,17),(4,17),(6,17),(8,17),(10,17),(2,18),(4,18),(6,18),(8,18),(10,18),(2,19),(4,19),(6,19),(8,19),(10,19),(2,20),(4,20),(6,20),(8,20),(10,20),(1,21),(11511110,11511111);
/*!40000 ALTER TABLE `participant_events` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`somay`@`localhost`*/ /*!50003 TRIGGER `participant_events_BEFORE_INSERT` BEFORE INSERT ON `participant_events` FOR EACH ROW BEGIN
DECLARE max_participants INT;
    DECLARE current_participants INT;
    
    SELECT NumberOfParticipants INTO max_participants FROM events WHERE EID = NEW.EID;

    SELECT COUNT(*) INTO current_participants FROM participant_events WHERE EID = NEW.EID;
    
    
    IF max_participants > 0 AND current_participants > max_participants THEN
        
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Maximum participants limit exceeded for this event!';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-20  1:23:48
