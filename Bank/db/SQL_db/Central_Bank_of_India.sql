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
-- Table structure for table `Central Bank of India`
--

CREATE TABLE IF NOT EXISTS `Central Bank of India` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Central Bank of India`
--

INSERT INTO `Central Bank of India` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/en/thumb/0/06/Central_Bank_of_India.svg/220px-Central_Bank_of_India.svg.png'),
('Type', 'Public company BSE & NSE :CENTRALBK '),
('Industry', 'Financial Commercial banks '),
('Founded', '21 December 1911 ; 103 years ago ( 1911-12-21 ) '),
('Headquarters', 'Mumbai , India '),
('Key people', 'Shri. Rajeev Rishi, Chairman & Managing Director '),
('Revenue', '191495 million (US$3.0 billion) (2010-11) '),
('Number of employees', '42000(approx) '),
('Website', 'www.centralbankofindia.co.in ');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
