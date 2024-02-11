CREATE INDEX indexPlayerPlayerid ON Player(playerid);
CREATE INDEX indexRankingFkPlayerid ON Ranking(FK_playerid);
CREATE INDEX indexMatchesFkPlayerone ON Matches(FK_playerOne);
CREATE INDEX indexMatchesFkPlayertwo ON Matches(FK_playerTwo);
CREATE INDEX indexMatchesWinnerid ON Matches(winnerID);