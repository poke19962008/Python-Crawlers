-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 21, 2015 at 08:28 PM
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
-- Table structure for table `State Bank of India`
--

CREATE TABLE IF NOT EXISTS `State Bank of India` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `State Bank of India`
--

INSERT INTO `State Bank of India` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/SBI-logo.svg/150px-SBI-logo.svg.png'),
('Type', 'Public '),
('Traded as', 'NSE : SBIN BSE : 500112 LSE : SBID BSE SENSEX Constituent CNX Nifty Constituent '),
('Industry', 'Banking , Financial Services '),
('Founded', '2 June 1956 , Nationalization , 1 July 1955  '),
('Headquarters', 'Mumbai , Maharashtra , India '),
('Area served', 'Worldwide '),
('Key people', 'Arundhati Bhattacharya ( Chairperson ) '),
('Products', 'consumer banking , corporate banking , finance and insurance , investment banking , mortgage loans , private banking , private equity , savings , Securities , asset management , wealth management , Cr'),
('Revenue', '210736 crore (US$33 billion) (2013)   '),
('Profit', '17916 crore (US$2.8 billion) (2013)   '),
('Total assets', '2374839 crore (US$370 billion) (2013)   '),
('Total equity', '98884 crore (US$16 billion) (2012)   '),
('Owner', 'Government of India '),
('Number of employees', '222,033 (2014) '),
('Slogan', 'The Banker to Every Indian '),
('Website', 'http://www.sbi.co.in/');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
