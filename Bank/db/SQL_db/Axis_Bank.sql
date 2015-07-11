-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 21, 2015 at 12:31 AM
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
-- Table structure for table `Axis Bank`
--

CREATE TABLE IF NOT EXISTS `Axis Bank` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Axis Bank`
--

INSERT INTO `Axis Bank` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/AXISBank_Logo.svg/220px-AXISBank_Logo.svg.png'),
('Traded as', 'BSE : 532215 LSE : AXBC NSE : AXISBANK '),
('Industry', 'Banking, Financial services '),
('Founded', '1994 (as UTI Bank) '),
('Headquarters', 'Mumbai , Maharashtra , India  '),
('Key people', '(Chairman) Shikha Sharma ( MD & CEO ) '),
('Products', 'Credit cards, consumer banking , corporate banking , finance and insurance , investment banking , mortgage loans , private banking , private equity , wealth management '),
('Revenue', '340 billion (US$5.3 billion) (2012)   '),
('Operating income', '94 billion (US$1.5 billion) (2012)   '),
('Net income', '52 billion (US$820 million) (2012)   '),
('Total assets', '3.4 trillion (US$53 billion) (2012)   '),
('Number of employees', '42,420 (on 31-March-2014)  '),
('Website', 'www.axisbank.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
