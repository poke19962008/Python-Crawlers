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
-- Table structure for table `ICICI Bank Limited`
--

CREATE TABLE IF NOT EXISTS `ICICI Bank Limited` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ICICI Bank Limited`
--

INSERT INTO `ICICI Bank Limited` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/commons/thumb/1/12/ICICI_Bank_Logo.svg/200px-ICICI_Bank_Logo.svg.png'),
('Type', 'Public company '),
('Traded as', 'BSE : 532174 NSE : ICICIBANK NYSE : IBN BSE SENSEX Constituent CNX Nifty Constituent '),
('Industry', 'Banking, Financial services '),
('Founded', '1994 ( 1994 ) '),
('Headquarters', 'Mumbai , Maharashtra , India '),
('Area served', 'Worldwide '),
('Key people', 'K. V. Kamath (Chairman) Ms. Chanda Kochhar (MD & CEO) '),
('Products', 'Credit cards, Consumer banking , corporate banking , finance and insurance , investment banking , mortgage loans , private banking , wealth management '),
('Revenue', 'US$ 8.255 billion (2014)  '),
('Operating income', 'US$ 0 1.934 billion (2014)  '),
('Profit', 'US$ 0 1.828 billion (2014)  '),
('Total assets', 'US$99 billion (2014)  '),
('Total equity', 'US$12.73 billion (2014)  '),
('Number of employees', '94,204 (2014)  '),
('Website', 'www.icicibank.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
