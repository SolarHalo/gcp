DROP TABLE  `game` ;
CREATE TABLE `game` (
  `id` integer NOT NULL AUTO_INCREMENT,
  `game_id` varchar(128) NOT NULL DEFAULT '',
  `game_name` varchar(100) DEFAULT NULL,
  `family` varchar(300) DEFAULT NULL,
  `genre_name` varchar(50) DEFAULT NULL,
  `shortdesc` varchar(1024) DEFAULT NULL,
  `meddesc` text DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `gamerank` varchar(50) DEFAULT NULL,
  `releasedate` timestamp ,
  `gamesize` varchar(30) DEFAULT NULL,
  `language` varchar(20) DEFAULT NULL,
  `longdesc` text,
  `site` varchar(10) DEFAULT NULL,
  `gametype` varchar(10) DEFAULT NULL,
  `systemreq` varchar(300) DEFAULT NULL,
  
  `bullet1` varchar(300) DEFAULT NULL, /*--游戏要点1--*/
  `bullet2` varchar(300) DEFAULT NULL, /*--游戏要点2--*/
  `bullet3` varchar(300) DEFAULT NULL, /*--游戏要点3--*/
  `bullet4` varchar(300) DEFAULT NULL, /*--游戏要点4--*/
  `bullet5` varchar(1024) DEFAULT NULL, /*--游戏要点5--*/
  
  `img_small` varchar(300) DEFAULT NULL, /*--小图 big60*40 alawar 44*44--*/
  `img_med` varchar(300) DEFAULT NULL, /*--小图 big80*80 alawar 100*100--*/
  `img_subfeature` varchar(300) DEFAULT NULL, /*--subfeature.jpg--*/
  `img_feature` varchar(300) DEFAULT NULL, /*--feature.jpg--*/
  `img_thumb1` varchar(300) DEFAULT NULL, /*--游戏截图1：小图--*/
  `img_thumb2` varchar(300) DEFAULT NULL, /*--游戏截图2：小图--*/
  `img_thumb3` varchar(300) DEFAULT NULL, /*--游戏截图3：小图--*/
  `img_screen1` varchar(300) DEFAULT NULL, /*--游戏截图1：大图--*/
  `img_screen2` varchar(300) DEFAULT NULL, /*--游戏截图2：大图--*/
  `img_screen3` varchar(300) DEFAULT NULL, /*--游戏截图3：大图--*/
  
  `video` varchar(300) DEFAULT NULL, /*--游戏视频--*/
  `flash` varchar(300) DEFAULT NULL, /*--游戏flash--*/
  `downloadurl` varchar(300) DEFAULT NULL, /*--下载链接--*/
  `buyurl` varchar(300) DEFAULT NULL, /*--购买链接--*/
  `downloadiframe` varchar(300) DEFAULT NULL, /*--下载框架链接--*/
  `buyiframe` varchar(300) DEFAULT NULL, /*--购买框架链接--*/
  
  `foldername` varchar(300) DEFAULT NULL, /*--语言_游戏标题（组合游戏路径用）--*/
  `timestamp` timestamp ,/*-- 采集时间 --*/
  
  PRIMARY KEY (`id`)
) CHARSET=utf8;


DROP TABLE  `game_feature` ;
CREATE TABLE `game_feature` (
  `id` integer NOT NULL AUTO_INCREMENT,
  `g_id` integer,
  `game_id` varchar(128) NOT NULL DEFAULT '',
  `language` varchar(20) DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `gametype` varchar(10) DEFAULT NULL, 
  
  `hasdwfeature` varchar(10) DEFAULT NULL, 
  `dwwidth` varchar(10) DEFAULT NULL, 
  `dwheight` varchar(10) DEFAULT NULL, 
  `gamerank` varchar(10) DEFAULT NULL, 
  `releasedate` timestamp, 
  `timestamp` timestamp ,/*-- 采集时间 --*/
  PRIMARY KEY (`id`)
) CHARSET=utf8;


DROP TABLE  `game_daily` ;
CREATE TABLE `game_daily` (
  `id` integer NOT NULL AUTO_INCREMENT,
  `g_id` integer,
  `game_id` varchar(128) NOT NULL DEFAULT '',
  `language` varchar(20) DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `gametype` varchar(10) DEFAULT NULL,
  `content` varchar(50) DEFAULT NULL,
  
  `title` varchar(200) DEFAULT NULL,
  `link` varchar(400) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `description` text,
  `pub_date` timestamp, 
  `timestamp` timestamp ,/*-- 采集时间 --*/
  PRIMARY KEY (`id`)
) CHARSET=utf8;

DROP TABLE  `game_catch` ;
CREATE TABLE `game_catch` (
  `id` integer NOT NULL AUTO_INCREMENT,
  `g_id` integer,
  `game_id` varchar(128) NOT NULL DEFAULT '',
  `language` varchar(20) DEFAULT NULL,
  `site` varchar(10) DEFAULT NULL,
  `gametype` varchar(10) DEFAULT NULL,
  
  `logo_url` varchar(200) DEFAULT NULL,
  `images_med` varchar(500) DEFAULT NULL,
  `tagline` varchar(100) DEFAULT NULL,
  `offer_start_date` timestamp, 
  `offer_end_date` timestamp, 
  `link` varchar(500) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `timestamp` timestamp ,/*-- 采集时间 --*/
  PRIMARY KEY (`id`)
) CHARSET=utf8;
