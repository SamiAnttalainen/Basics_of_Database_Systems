####################################################
############## Do not touch this part ##############
import sqlite3
db = sqlite3.connect('hw5tennis.db')
cur = db.cursor()
def initializeDB():
    try:
        f = open("sqlcommands.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization") 


def main():
    initializeDB()
    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Print Players")
        print("2: Print Ranking")
        print("3: Print Matches")
        print("4: Search for one player")
        print("5: Move matchdate")
        print("6: Delete player")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            printPlayers()
        if userInput == "2":
            printRanking()
        if userInput == "3":
            printMatches()
        if userInput == "4":
            searchPlayer()
        if userInput == "5":
            moveMatch()
        if userInput == "6":
            deletePlayer()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

############## Do not touch part ends ##############
####################################################


############## Please modify the following ##############
def printPlayers():
    print("Printing players")
    """
    Insert the correct Python and SQL commands
    to print all players
    """
    #Start your modifications after this comment
    #You should print the data noe row at a time.


    #Print player information row by row.
    cur.execute("SELECT * FROM Player")
    Players = cur.fetchall()
    for Player in Players:
        print(Player)

    return

def printRanking():
    print("Printing ranking")
    """
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    #Start your modifications after this comment
    #You should print the data noe row at a time.
    # Print ranking information row by row.

    cur.execute("SELECT * FROM Ranking")
    Rankings = cur.fetchall()
    for Ranking in Rankings:
        print(Ranking)

    return

def printMatches():
    print("Printing matches")
    """ 
    Insert the correct Python and SQL commands 
    to print all ranking information
    """
    #Start your modifications after this comment
    #You should print the data one row at a time.
    # Print match information row by row.
    cur.execute("SELECT * FROM Matches")
    Matches = cur.fetchall()
    for Match in Matches:
        print(Match)

    return

def searchPlayer():
    playerName = input("What is the player's surname? ")
    """ 
    Insert the correct Python and SQL commands to find the player 
    using the given surname
    """
    #Start your modifications after this comment
    #You are given the print statements, now you need to add the fetched data to the five prints.
    
    # The search is done based on player surname and as an output, you should print the player's data on separate rows (print rows are included in the template).
    cur.execute("SELECT * FROM Player WHERE last_name = ?", (playerName,))
    Player = cur.fetchone()

    print("ID: " + str(Player[0]))
    print("First name:" + str(Player[1]))
    print("Last name:" + str(Player[2]))
    print("Birthdate: "+ str(Player[4]))
    print("Nationality:"+ str(Player[3]))



    return

def moveMatch():
    matchID = input("What is the matchID of the match you want to move? ")
    newMatchDate = input ("What is the new matchdate you want to set?")
    
    """ 
    Using the correct Python and SQL comands:
    Change the match date based on the given matchID and new matchdate
    IF a new matchdate is set to NULL, set the winner and result to NULL as well
    """
    #Start your modifications after this comment
    # The match date can also be set to NULL. If this is done, it means that the match has not been played so you need to NULL the winner and score as well.
    cur.execute("UPDATE Matches SET matchdate = ? WHERE matchid = ?", (newMatchDate, matchID))
    db.commit()
    if newMatchDate == "NULL":
        cur.execute("UPDATE Matches SET winnerID = NULL WHERE matchid = ?", (matchID,))
        db.commit()
        cur.execute("UPDATE Matches SET resultSets = NULL WHERE matchid = ?", (matchID,))
        db.commit()
        cur.execute("UPDATE Matches SET matchdate = NULL WHERE matchid = ?", (matchID,))
        db.commit()
    


    return

def deletePlayer():
    playerID = input("What is the player's PlayerID? ")
    """ 
    Using the correct Python and SQL comands:
    Delete the Player and his Ranking information
    Additionally, set the playerid to NULL in ALL match-data it is found
    """
    #Start your modifications after this comment
    # When deleting the player, make sure the ranking table is also modified (remove the player information)
    #  and modify the match information (set NULL the player ID in all instances where the removed player appears).
    cur.execute("DELETE FROM Player WHERE playerid = ?", (playerID,))
    cur.execute("DELETE FROM Ranking WHERE FK_playerid = ?", (playerID,))
    cur.execute("UPDATE Matches SET FK_playerOne = NULL WHERE FK_PlayerOne = ?", (playerID,))
    cur.execute("UPDATE Matches SET FK_playerTwo = NULL WHERE FK_PlayerTwo = ?", (playerID,))
    cur.execute("UPDATE Matches SET winnerID = NULL WHERE winnerID = ?", (playerID,))
    db.commit()

main()