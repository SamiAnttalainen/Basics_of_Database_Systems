SELECT * FROM Player
INNER JOIN Ranking ON Player.playerid == Ranking.rankingid
WHERE points > 7 AND rank <= 10
LIMIT 10;