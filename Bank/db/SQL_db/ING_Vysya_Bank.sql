-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 20, 2015 at 03:28 PM
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
-- Table structure for table `ING Vysya Bank`
--

CREATE TABLE IF NOT EXISTS `ING Vysya Bank` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ING Vysya Bank`
--

INSERT INTO `ING Vysya Bank` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/en/thumb/3/3e/ING_Vysya_Bank.svg/220px-ING_Vysya_Bank.svg.png'),
('Type', 'Public BSE : 531807 '),
('Industry', 'Banking, Financial Services & insurance '),
('Founded', '2002 (est. 1930 as Vysya Bank ) '),
('Headquarters', 'Bangalore , India '),
('Key people', 'Shailendra Bhandari(CEO & MD) Uday Sareen (deputy CEO) Arun Thiagarajan (Chairman of the Board) '),
('Revenue', '5588 crore (US$880 million)  '),
('Total assets', '54836 crore (US$8.6 billion)  '),
('Number of employees', 'Over 10,000  No. of Branches: 527  No. of ATMS: 405 No. of Extension counters: 10 '),
('Website', 'ING Vysya Bank ');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
