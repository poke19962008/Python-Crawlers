-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 30, 2015 at 11:27 PM
-- Server version: 5.6.21
-- PHP Version: 5.6.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `SRM_SE`
--

-- --------------------------------------------------------

--
-- Table structure for table `BARCLAYS`
--

CREATE TABLE IF NOT EXISTS `BARCLAYS` (
  `LP` varchar(4) NOT NULL,
  `IMG` varchar(200) DEFAULT NULL,
  `GF` tinyint(4) NOT NULL,
  `CLUB` varchar(100) NOT NULL,
  `PTS` tinyint(4) NOT NULL,
`POS` tinyint(4) NOT NULL,
  `L` tinyint(4) NOT NULL,
  `P` tinyint(4) NOT NULL,
  `GD` tinyint(4) NOT NULL,
  `W` tinyint(4) NOT NULL,
  `GA` tinyint(4) NOT NULL,
  `D` tinyint(4) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `BARCLAYS`
--

INSERT INTO `BARCLAYS` (`LP`, `IMG`, `GF`, `CLUB`, `PTS`, `POS`, `L`, `P`, `GD`, `W`, `GA`, `D`) VALUES
('(1)', 'null', 68, 'Chelsea', 80, 1, 2, 34, 41, 24, 27, 8),
('(2)', 'null', 70, 'Manchester City', 67, 2, 7, 34, 34, 20, 36, 7),
('(3)', 'null', 63, 'Arsenal', 67, 3, 6, 33, 31, 20, 32, 7),
('(4)', 'null', 59, 'Manchester United', 65, 4, 7, 34, 25, 19, 34, 8),
('(5)', 'null', 47, 'Liverpool', 58, 5, 10, 34, 10, 17, 37, 7),
('(6)', 'null', 55, 'Tottenham Hotspur', 58, 6, 10, 34, 6, 17, 49, 7),
('(7)', 'null', 47, 'Southampton', 57, 7, 11, 34, 21, 17, 26, 6),
('(8)', 'null', 41, 'Swansea City', 50, 8, 12, 34, -3, 14, 44, 8),
('(9)', 'null', 39, 'Stoke City', 47, 9, 13, 34, -3, 13, 42, 8),
('(10)', 'null', 44, 'Everton', 44, 10, 12, 34, 1, 11, 43, 11),
('(11)', 'null', 42, 'West Ham United', 44, 11, 12, 34, 0, 11, 42, 11),
('(12)', 'null', 42, 'Crystal Palace', 42, 12, 14, 34, -5, 11, 47, 9),
('(13)', 'null', 32, 'West Bromwich Albion', 37, 13, 15, 34, -14, 9, 46, 10),
('(14)', 'null', 36, 'Newcastle United', 35, 14, 17, 34, -21, 9, 57, 8),
('(15)', 'null', 32, 'Hull City', 34, 15, 16, 34, -13, 8, 45, 10),
('(16)', 'null', 26, 'Aston Villa', 32, 16, 18, 34, -22, 8, 48, 8),
('(17)', 'null', 36, 'Leicester City', 31, 17, 19, 34, -18, 8, 54, 7),
('(18)', 'null', 26, 'Sunderland', 30, 18, 13, 33, -23, 5, 49, 15),
('(19)', 'null', 38, 'Queens Park Rangers', 27, 19, 21, 34, -21, 7, 59, 6),
('(20)', 'null', 26, 'Burnley', 26, 20, 18, 34, -26, 5, 52, 11);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `BARCLAYS`
--
ALTER TABLE `BARCLAYS`
 ADD PRIMARY KEY (`POS`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `BARCLAYS`
--
ALTER TABLE `BARCLAYS`
MODIFY `POS` tinyint(4) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
