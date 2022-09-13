CREATE DATABASE IF NOT EXISTS SingalPageWebSql;

use SingalPageWebSql;

CREATE USER 'WebPageSqlUser'@'%' IDENTIFIED BY '3c5806f50df69ed06da2fa76bf1730da';
GRANT CREATE,INSERT,UPDATE,SELECT ON SingalPageWebSql.* TO 'WebPageSqlUser'@'%';

CREATE TABLE `signin` (
  `id` int AUTO_INCREMENT,
  `ip` varchar(255) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `comment`(
    `id` int AUTO_INCREMENT,
    `ip` LONGTEXT NOT NULL,
    `videoName` LONGTEXT NOT NULL,
    `text` LONGTEXT NOT NULL,
    `datetime` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);



ALTER TABLE signin CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE comment CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;


FLUSH PRIVILEGES;