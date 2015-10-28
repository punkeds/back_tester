CREATE TABLE IF NOT EXISTS `brent` (
  `ticker` varchar(256) NOT NULL,
  `per` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `open` decimal(10,0) NOT NULL,
  `high` decimal(10,0) NOT NULL,
  `low` decimal(10,0) NOT NULL,
  `close` decimal(10,0) NOT NULL,
  `vol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;