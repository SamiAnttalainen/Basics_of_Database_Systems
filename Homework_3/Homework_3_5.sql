CREATE TRIGGER hashtag_not_allowed BEFORE INSERT ON Hashtag
FOR EACH ROW
WHEN NEW.Content LIKE '%mayonnaise%'
BEGIN
    SELECT RAISE(ABORT, 'Mayonnaise detected!');
END;