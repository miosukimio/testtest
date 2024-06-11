/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80033 (8.0.33)
 Source Host           : localhost:3306
 Source Schema         : flask_web

 Target Server Type    : MySQL
 Target Server Version : 80033 (8.0.33)
 File Encoding         : 65001

 Date: 29/05/2024 14:05:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for exercises
-- ----------------------------
DROP TABLE IF EXISTS `exercises`;
CREATE TABLE `exercises`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of exercises
-- ----------------------------
INSERT INTO `exercises` VALUES (1, '五十音');
INSERT INTO `exercises` VALUES (2, '习题2');

-- ----------------------------
-- Table structure for h_category
-- ----------------------------
DROP TABLE IF EXISTS `h_category`;
CREATE TABLE `h_category`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of h_category
-- ----------------------------
INSERT INTO `h_category` VALUES (1, '母音');
INSERT INTO `h_category` VALUES (2, 'K行');
INSERT INTO `h_category` VALUES (3, 'S行');
INSERT INTO `h_category` VALUES (4, 'T行');
INSERT INTO `h_category` VALUES (5, 'N行');
INSERT INTO `h_category` VALUES (6, 'H行');

-- ----------------------------
-- Table structure for hiragana
-- ----------------------------
DROP TABLE IF EXISTS `hiragana`;
CREATE TABLE `hiragana`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `file` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `category_id`(`category_id` ASC) USING BTREE,
  CONSTRAINT `hiragana_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `h_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of hiragana
-- ----------------------------
INSERT INTO `hiragana` VALUES (8, 'あ', '/media/sounds/a.mp3', 1);
INSERT INTO `hiragana` VALUES (9, 'い', '/media/sounds/i.mp3', 1);
INSERT INTO `hiragana` VALUES (10, 'う', '/media/sounds/u.mp3', 1);
INSERT INTO `hiragana` VALUES (11, 'え', '/media/sounds/e.mp3', 1);
INSERT INTO `hiragana` VALUES (12, 'お', '/media/sounds/o.mp3', 1);
INSERT INTO `hiragana` VALUES (13, 'か', '/media/sounds/test.mp3', 2);
INSERT INTO `hiragana` VALUES (14, 'き', '/media/sounds/test.mp3', 2);

-- ----------------------------
-- Table structure for q_category
-- ----------------------------
DROP TABLE IF EXISTS `q_category`;
CREATE TABLE `q_category`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `e_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE,
  INDEX `e_id`(`e_id` ASC) USING BTREE,
  CONSTRAINT `q_category_ibfk_1` FOREIGN KEY (`e_id`) REFERENCES `exercises` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of q_category
-- ----------------------------
INSERT INTO `q_category` VALUES (1, '类别1', 1);
INSERT INTO `q_category` VALUES (2, '类别2', 1);
INSERT INTO `q_category` VALUES (3, '类别3', 1);

-- ----------------------------
-- Table structure for quiz
-- ----------------------------
DROP TABLE IF EXISTS `quiz`;
CREATE TABLE `quiz`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `opt1` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `opt2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `opt3` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `opt4` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `correct` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `file` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `category_id`(`category_id` ASC) USING BTREE,
  CONSTRAINT `quiz_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `q_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of quiz
-- ----------------------------
INSERT INTO `quiz` VALUES (1, '题目11111111111', 'a', 'b', 'c', 'd', 'a', '/media/sounds/a.mp3', 1);
INSERT INTO `quiz` VALUES (2, '题目2', '22', '33', '44', 'aa', '22', NULL, 1);
INSERT INTO `quiz` VALUES (3, '题目3333', 'う', 'え', 'あ', 'い', 'い', NULL, 1);
INSERT INTO `quiz` VALUES (4, '题目1111', '3', '5', '6', '7', '7', NULL, 2);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `hiragana_dic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `hiragana_time` datetime NULL DEFAULT NULL,
  `last_video` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `video_time` datetime NULL DEFAULT NULL,
  `score_dic` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `is_admin` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'admin', 'admin', '110', '110@qq.com', '{8: 3, 9: 1, 10: 1}', '2024-05-28 17:56:17', '1', '2024-05-28 16:19:39', '{1: {\'score\': 3, \'time\': \'2024-05-28 16:20:11\'}}', 1);
INSERT INTO `user` VALUES (2, 'test1', 'test1', '111', '111@qq.com', '{8: 3, 14: 5, 10: 10, 11: 1, 13: 18}', '2024-05-28 17:32:44', '2', '2024-05-28 15:37:54', '{1: {\'score\': 2, \'time\': \'2024-05-28 17:45:52\'}, 2: {\'score\': 2, \'time\': \'2024-05-28 15:37:45\'}}', 0);

-- ----------------------------
-- Table structure for v_category
-- ----------------------------
DROP TABLE IF EXISTS `v_category`;
CREATE TABLE `v_category`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of v_category
-- ----------------------------
INSERT INTO `v_category` VALUES (1, '初级');
INSERT INTO `v_category` VALUES (2, '中级');
INSERT INTO `v_category` VALUES (3, '高级');

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `file` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `introduce` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `category_id`(`category_id` ASC) USING BTREE,
  CONSTRAINT `video_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `v_category` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of video
-- ----------------------------
INSERT INTO `video` VALUES (1, '学习日语的基本发音，掌握正确的发音方法。', '/media/video/test.mp4', '基础发音教程', 1);
INSERT INTO `video` VALUES (2, 'test2', '/media/video/test.mp4', '这是一条介绍', 1);
INSERT INTO `video` VALUES (3, 'test2', '/media/video/test.mp4', '这是一条介绍11111111111111111111', 2);

SET FOREIGN_KEY_CHECKS = 1;
