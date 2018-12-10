-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- 생성 시간: 18-12-10 20:22
-- 서버 버전: 5.7.24-0ubuntu0.16.04.1
-- PHP 버전: 7.0.32-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 데이터베이스: `ITProj`
--

-- --------------------------------------------------------

--
-- 테이블 구조 `assa_board`
--

CREATE TABLE `assa_board` (
  `board_num` int(11) NOT NULL,
  `a_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `a_link` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `a_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `coolen_board`
--

CREATE TABLE `coolen_board` (
  `board_num` int(11) NOT NULL,
  `c_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `c_text` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `c_link` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `c_date` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `notice_board`
--

CREATE TABLE `notice_board` (
  `board_num` int(11) NOT NULL,
  `n_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `n_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `n_date` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `pang_board`
--

CREATE TABLE `pang_board` (
  `board_num` int(11) NOT NULL,
  `p_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `p_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `p_date` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `p_text` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `quei_board`
--

CREATE TABLE `quei_board` (
  `board_num` int(11) NOT NULL,
  `q_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `q_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `q_date` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `q_text` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- 테이블 구조 `seven_board`
--

CREATE TABLE `seven_board` (
  `board_num` int(11) NOT NULL,
  `s_title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `s_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `s_date` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `s_text` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 덤프된 테이블의 인덱스
--

--
-- 테이블의 인덱스 `assa_board`
--
ALTER TABLE `assa_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 테이블의 인덱스 `coolen_board`
--
ALTER TABLE `coolen_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 테이블의 인덱스 `notice_board`
--
ALTER TABLE `notice_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 테이블의 인덱스 `pang_board`
--
ALTER TABLE `pang_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 테이블의 인덱스 `quei_board`
--
ALTER TABLE `quei_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 테이블의 인덱스 `seven_board`
--
ALTER TABLE `seven_board`
  ADD PRIMARY KEY (`board_num`);

--
-- 덤프된 테이블의 AUTO_INCREMENT
--

--
-- 테이블의 AUTO_INCREMENT `assa_board`
--
ALTER TABLE `assa_board`
  MODIFY `board_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
--
-- 테이블의 AUTO_INCREMENT `coolen_board`
--
ALTER TABLE `coolen_board`
  MODIFY `board_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=186;
--
-- 테이블의 AUTO_INCREMENT `pang_board`
--
ALTER TABLE `pang_board`
  MODIFY `board_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;
--
-- 테이블의 AUTO_INCREMENT `quei_board`
--
ALTER TABLE `quei_board`
  MODIFY `board_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;
--
-- 테이블의 AUTO_INCREMENT `seven_board`
--
ALTER TABLE `seven_board`
  MODIFY `board_num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=179;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
