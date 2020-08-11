/*
Navicat MySQL Data Transfer

Source Server         : 192.168.3.187
Source Server Version : 50725
Source Host           : 192.168.3.187:3306
Source Database       : Coffee_System

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-04-13 17:18:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for User_info_eq_info
-- ----------------------------
DROP TABLE IF EXISTS `User_info_eq_info`;
CREATE TABLE `User_info_eq_info` (
  `machine_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `mac_addr` varchar(64) NOT NULL,
  `addr` varchar(128) NOT NULL,
  `position` varchar(64) NOT NULL,
  `install_date` date NOT NULL,
  `install_emp_id` varchar(16) NOT NULL,
  `status` int(11) NOT NULL,
  `mantain_emp_id` varchar(16) NOT NULL,
  PRIMARY KEY (`machine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of User_info_eq_info
-- ----------------------------
INSERT INTO `User_info_eq_info` VALUES ('1', '1', '嘉熙业广场11楼1128_001', 'BC-EE-7B-5B-6B-0F', '嘉熙业广场11楼1128', '22.6290598194,114.0463683908', '2019-04-10', '梁胜云', '1', '林九峰');
INSERT INTO `User_info_eq_info` VALUES ('2', '1', '龙华广场8楼0802_001', 'BC-EE-7B-5B-6B-2F', '龙华广场8楼0802', '22.6609131320,114.0456618297', '2019-04-10', '郭洪山', '1', '林九峰');
INSERT INTO `User_info_eq_info` VALUES ('3', '1', '天汇大厦10楼1018_001', 'BC-EE-7B-5B-6B-3F', '天汇大厦10楼1018', '22.6490141267,114.0521801787', '2019-04-10', '张达', '1', '林九峰');
