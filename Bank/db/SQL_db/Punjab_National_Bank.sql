-- phpMyAdmin SQL Dump
-- version 4.2.11
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 20, 2015 at 03:29 PM
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
-- Table structure for table `Punjab National Bank`
--

CREATE TABLE IF NOT EXISTS `Punjab National Bank` (
  `HEADER` varchar(200) DEFAULT NULL,
  `VALUE` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Punjab National Bank`
--

INSERT INTO `Punjab National Bank` (`HEADER`, `VALUE`) VALUES
('Img Url', 'http://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Punjab_National_Bank.svg/200px-Punjab_National_Bank.svg.pngThe name you can BANK upon! '),
('Type', 'Public '),
('Traded as', 'BSE : 532461 NSE : PNB CNX Nifty Constituent '),
('Industry', 'Banking , Financial services '),
('Founded', '19 May 1894   '),
('Founder', 'Lala Lajpat Rai '),
('Headquarters', 'New Delhi, Delhi, India '),
('Key people', 'Gauri Shankar (Executive Director with additional charge of MD & CEO) '),
('Products', 'Credit cards, consumer banking , corporate banking , finance and insurance , investment banking , mortgage loans , private banking , private equity , wealth management '),
('Revenue', '47400 crore (US$7.4 billion)(2013)   '),
('Net income', 'INR 49.54 billion ( million) (2013)   '),
('Total assets', '( billion) (2013)   '),
('Owner', 'Government of India '),
('Number of employees', '62,392 (March 2013)  '),
('Website', 'www.pnbindia.in');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
