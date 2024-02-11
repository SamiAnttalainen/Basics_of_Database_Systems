.headers on

SELECT 
    PlayerOne.first_name || ' ' || PlayerOne.last_name AS "Player one", 
    PlayerTwo.first_name || ' ' || PlayerTwo.last_name AS "Player two", 
    M.matchdate AS "Matchdate", 
    Winner.first_name || ' ' || Winner.last_name AS Winner
FROM 
    Matches M
INNER JOIN 
    Player PlayerOne ON M.FK_playerOne = PlayerOne.playerid
INNER JOIN 
    Player PlayerTwo ON M.FK_playerTwo = PlayerTwo.playerid
INNER JOIN 
    Player Winner ON M.winnerID = Winner.playerid
WHERE 
    ((M.FK_playerOne, M.FK_playerTwo) IN (
        SELECT playerOne, playerTwo
        FROM (
            SELECT FK_playerOne AS playerOne, FK_playerTwo AS playerTwo
            FROM Matches
            UNION ALL
            SELECT FK_playerTwo AS playerOne, FK_playerOne AS playerTwo
            FROM Matches
        )
        GROUP BY playerOne, playerTwo
        HAVING COUNT(*) > 1
    ))
ORDER BY 
    Winner, M.matchid;