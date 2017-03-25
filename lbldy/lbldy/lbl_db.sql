/*
Navicat MySQL Data Transfer

Source Server         : aa
Source Server Version : 50605
Source Host           : localhost:3306
Source Database       : spider_demo

Target Server Type    : MYSQL
Target Server Version : 50605
File Encoding         : 65001

Date: 2017-03-25 10:48:31
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lbl_db
-- ----------------------------
DROP TABLE IF EXISTS `lbl_db`;
CREATE TABLE `lbl_db` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '电影名称',
  `summary` varchar(2000) DEFAULT NULL COMMENT '电影简介',
  `link` varchar(1000) DEFAULT NULL COMMENT '下载链接',
  `website` varchar(255) DEFAULT '' COMMENT '电影下载页面',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9439 DEFAULT CHARSET=utf8;
