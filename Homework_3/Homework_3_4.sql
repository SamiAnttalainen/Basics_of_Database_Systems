DROP VIEW IF EXISTS Comments_of_comments;
CREATE VIEW Comments_of_comments AS 
SELECT 
    User.Username AS User,
    Comment_1.Content AS Comment,
    Comment_2.CommentID AS "Commented on"
FROM 
    User User
INNER JOIN 
    Comments Comment_1 ON User.UserID = Comment_1.UserID
INNER JOIN 
    Comments Comment_2 ON Comment_1.FK_CommentID = Comment_2.CommentID
ORDER BY 
    User ASC, 
    "Commented on" DESC;

SELECT * FROM Comments_of_comments;