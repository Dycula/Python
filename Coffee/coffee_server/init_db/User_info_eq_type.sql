/*
Navicat MySQL Data Transfer

Source Server         : 192.168.3.187
Source Server Version : 50725
Source Host           : 192.168.3.187:3306
Source Database       : Coffee_System

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-04-13 17:18:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for User_info_eq_type
-- ----------------------------
DROP TABLE IF EXISTS `User_info_eq_type`;
CREATE TABLE `User_info_eq_type` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `size` varchar(64) NOT NULL,
  `weight` decimal(8,2) NOT NULL,
  `power` varchar(32) NOT NULL,
  `dissipation` int(11) NOT NULL,
  `material_buckets` int(11) NOT NULL,
  `water_proofing_grade` varchar(16) NOT NULL,
  `pipe_standard` varchar(16) NOT NULL,
  `inflow_pressue` varchar(16) NOT NULL,
  `work_temperature` varchar(16) NOT NULL,
  `screen_size` decimal(8,2) NOT NULL,
  `comm_interface` varchar(32) NOT NULL,
  `os` varchar(32) NOT NULL,
  `payment_cate` varchar(32) NOT NULL,
  `data_standard` varchar(32) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of User_info_eq_type
-- ----------------------------
INSERT INTO `User_info_eq_type` VALUES ('1', 'ES4C', '700(H)*420(W)*450(D)mm', '60.00', 'AC220V/50HZ', '2700', '3', 'IPX1', 'G3/8', '0.5-7bar', '75', '14.00', 'USB,WIFI,4G', 'LINUX系统、Android系统', '微信、支付宝', 'EVA-DTS');
