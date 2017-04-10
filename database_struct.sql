-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Gostitelj: localhost
-- Čas nastanka: 10. apr 2017 ob 15.10
-- Različica strežnika: 10.1.16-MariaDB
-- Različica PHP: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;



-- --------------------------------------------------------

--
-- Struktura tabele `today_matches`
--

CREATE TABLE `today_matches` (
  `id` int(11) NOT NULL,
  `date` text COLLATE utf8_slovenian_ci NOT NULL,
  `teams` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_1_out_prediction` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_x_out_prediction` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_2_out_prediction` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_tips_out_prediction` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_odds_1` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_odds_x` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_odds_2` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_odds_u2_5` text COLLATE utf8_slovenian_ci NOT NULL,
  `prva_odds_o2_5` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_matches` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_avg_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_0_1_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_2_3_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_4_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_1_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_1_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_2_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_2_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_3_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_3_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_4_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_under_over_4_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_0` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_1p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_2p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_3p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_4p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_6p` text COLLATE utf8_slovenian_ci NOT NULL,
  `druga_total_goals_7p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_matches` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_avg_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_0_1_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_2_3_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_4_goals` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_1_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_1_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_2_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_2_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_3_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_3_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_4_5m` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_under_over_4_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_0` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_1p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_2p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_3p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_4p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_5p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_6p` text COLLATE utf8_slovenian_ci NOT NULL,
  `tretja_total_goals_7p` text COLLATE utf8_slovenian_ci NOT NULL,
  `match_date` text COLLATE utf8_slovenian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_slovenian_ci;

--
-- Indeksi zavrženih tabel
--

--
-- Indeksi tabele `today_matches`
--
ALTER TABLE `today_matches`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT zavrženih tabel
--

--
-- AUTO_INCREMENT tabele `today_matches`
--
ALTER TABLE `today_matches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
