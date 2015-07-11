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
-- Table structure for table `Bank of Baroda`
--

CREATE TABLE IF NOT EXISTS `Bank of Baroda` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Bank of Baroda`
--

INSERT INTO `Bank of Baroda` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/en/thumb/f/f2/BankOfBarodaLogo.svg/250px-BankOfBarodaLogo.svg.png'),
('Type', 'Public '),
('Traded as', 'BSE : 532134 '),
('Industry', 'Banking, Financial services '),
('Founded', '20 July 1908 ( 1908-07-20 ) '),
('Founder', 'Maharaja Sayajirao Gaekwad  '),
('Headquarters', 'Vadodara (Baroda), Gujarat , India '),
('Area served', 'Worldwide '),
('Key people', '(Chairman & MD ) '),
('Products', 'Credit cards, consumer banking , corporate banking , finance and insurance , investment banking , mortgage loans , private banking , private equity , wealth management '),
('Revenue', '346 billion (US$5.4 billion) (2012)  '),
('Net income', '52.48 billion (US$820 million) (2012)  '),
('Total assets', '4.574 trillion (US$72 billion) (2012)  '),
('Website', 'www.bankofbaroda.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
