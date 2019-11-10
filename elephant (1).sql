-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 10, 2019 at 08:11 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elephant`
--

-- --------------------------------------------------------

--
-- Table structure for table `dece`
--

CREATE TABLE `dece` (
  `cerno` varchar(255) NOT NULL,
  `oname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `identity`
--

CREATE TABLE `identity` (
  `Ename` varchar(255) NOT NULL,
  `CerNo` varchar(255) NOT NULL,
  `Mno` varchar(255) NOT NULL,
  `MRno` varchar(255) NOT NULL,
  `Age` int(11) NOT NULL,
  `Sex` varchar(255) NOT NULL,
  `Oname` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `MigStat` varchar(255) NOT NULL,
  `Observation` varchar(500) NOT NULL,
  `sysdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `officials`
--

CREATE TABLE `officials` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `owner`
--

CREATE TABLE `owner` (
  `oid` int(11) NOT NULL,
  `oname` varchar(255) NOT NULL,
  `opwd` varchar(255) NOT NULL,
  `oaddress` varchar(255) NOT NULL,
  `ophone` varchar(255) NOT NULL,
  `ele_no` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `physique`
--

CREATE TABLE `physique` (
  `CerNo` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `Ecolor` varchar(255) NOT NULL,
  `Height` int(11) NOT NULL,
  `Length_tt` int(11) NOT NULL,
  `Ngirth` int(11) NOT NULL,
  `Cgirth` int(11) NOT NULL,
  `Weight` int(11) NOT NULL,
  `FRnail` int(11) NOT NULL,
  `HRnail` int(11) NOT NULL,
  `FLnail` int(11) NOT NULL,
  `HLnail` int(11) NOT NULL,
  `MolSet` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dece`
--
ALTER TABLE `dece`
  ADD PRIMARY KEY (`cerno`);

--
-- Indexes for table `identity`
--
ALTER TABLE `identity`
  ADD PRIMARY KEY (`CerNo`),
  ADD UNIQUE KEY `CerNo` (`CerNo`);

--
-- Indexes for table `officials`
--
ALTER TABLE `officials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `owner`
--
ALTER TABLE `owner`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `physique`
--
ALTER TABLE `physique`
  ADD PRIMARY KEY (`CerNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `owner`
--
ALTER TABLE `owner`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
