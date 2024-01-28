
DROP VIEW IF EXISTS Tweets_and_tags;
CREATE VIEW Tweets_and_tags AS 
SELECT 
    User.Username AS User,
    Tweet.Content AS Tweet,
    COALESCE(GROUP_CONCAT(Hashtag.Content, ''), '') AS Hashtag
FROM 
    User User
INNER JOIN 
    Tweet Tweet ON User.UserID = Tweet.UserID
LEFT JOIN 
    HashtagsInContent HC ON Tweet.TweetID = HC.TweetID
LEFT JOIN 
    Hashtag Hashtag ON HC.HashtagID = Hashtag.HashtagID
GROUP BY 
    User.Username, Tweet.Content
HAVING
    Hashtag != ''
ORDER BY 
    User ASC;
SELECT * FROM Tweets_and_tags;