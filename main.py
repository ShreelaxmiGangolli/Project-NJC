#shreelaxmi s gangolli
#canara engineering college

import sqlite3
import sys
import os
os.system("")
from time import sleep

# Connects to database
def connectDatabase():
    return sqlite3.connect("Date.db")
db=connectDatabase()
cursor=connectDatabase().cursor()

## inserting  data Into Database
def datainsert(db):
    movie_name = input("Enter Movie: ")
    actor = input("Enter Actor name: ")
    actress = input("Enter actress name: ")
    director = input("Enter director name: ")
    year = input("Enter year of release: ")
    cmd = ("""INSERT INTO database (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    parms =(movie_name,actor,actress,director,year)
    cursor.execute(cmd,parms)
    db.commit()
    print(  "\nData saved. ) ")


## function to remove data from Database
def RemoveData(db):
    cursor.execute("""DELETE FROM database;""").fetchall()
    db.commit()
    print( "Data Deleted!" )


##  Find movies by an Actor
def find_actor():
    act=str(input("Enter Actor Name : "))
    c=cursor.execute("""SELECT movie FROM database WHERE actor=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
        print( "No Actor Found." )


##  Find movies by an Actress
def find_actress():
    act = str(input("Enter Actress Name : "))
    c = cursor.execute("""SELECT movie FROM database WHERE actress=(?);""",(act,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + "No Actress Found : (" + style.END)



##  Find Movies By a Director
def find_director():
    director=str(input("Enter the director name : "))
    c=cursor.execute("""SELECT movie FROM database WHERE director=(?);""",(director,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + "No Dicrectors Found : (" + style.END)

##  Find Movies By a Year
def find_year():
    year = str(input("Enter the release year : "))
    c = cursor.execute("""SELECT movie FROM database WHERE year=(?);""",(year,)).fetchall()
    db.commit()
    for i in c:
        print(i,end='')
    if c==[]:
         print(style.RED + "No Movies Found : (" + style.END)



##  displaying database
def displayDatabase():
    Movie =  []
    Actor = []
    Actress  = []
    Director = []
    Year = []
    data=cursor.execute("""SELECT * FROM database; """).fetchall()
    print( "Movie" + " | " + "Actor" + " | " + "Actress" +  " | " + "Director" + " | " + "Year" )
    #printing data
    for row in data:
        Movie.append(row[0])
        Actor.append(row[1])
        Actress.append(row[2])
        Director.append(row[3])
        Year.append(row[4])
    print("Movie = ", Movie)
    print("Actor = ", Actor)
    print("Actress  = ",Actress)
    print("Director  = ", Director)
    print("Year  = ", Year)


# creating Table
def createTable(db):
    t = cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="database" ; """).fetchall()
    if t == []:
        cursor.execute("""CREATE TABLE IF NOT EXISTS database(movie VARCHAR(50),actor VARCHAR(20), actress VARCHAR(20), director VARCHAR(20),year INT);""")
        print( 'Table Created !' )
        db.commit()
    else:
        print( 'Table Already Exist.')

## checking Data connection
def testConnection():
    if connectDatabase() is not None:
        print( "Connected." )
        createTable(connectDatabase())
    else:
        print( " No Database is not connected." )
#clearing screen
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')


## main function
def main():
    while(1):
        clrscr()
        print(" **************************************************************************"  )
        print("*                    Movie Database by Shreelaxmi                         *" )
        print(" ******************************************************************" )
        print(" 1. Is the DataBase Connected ?")
        print(" 2. Insert data                                      ")
        print(" 3. Delete data                                      ")
        print(" 4. Show data                                        ")
        print(" 5. Movies by Actor                                  ")
        print(" 6. Movies by Actress                                ")
        print(" 7. Movies by Director                               ")
        print(" 8. Movies of year                                   ")
        print(" 9. Exit                                             ")
        print(" ******************************************************************" )
        choice=input("\nEnter your choice ")
        print('*******************************************************************' )
        if choice=='1':
            clrscr()
            testConnection()
            sleep(2)
        elif choice=='2':
            clrscr()
            datainsert(connectDatabase())
            sleep(2)
        elif choice=='3':
            clrscr()
            RemoveData()
            sleep(2)
        elif choice=='4':
            clrscr()
            displayDatabase()
            sleep(10)
        elif choice=='5':
            clrscr()
            find_actor()
            sleep(2)
        elif choice=='6':
            clrscr()
            find_actress()
            sleep(2)
        elif choice=='7':
            clrscr()
            find_director()
            sleep(2)
        elif choice=='8':
            clrscr()
            find_year()
            sleep(2)
        elif choice=='9':
            clrscr()
            print("End.")
            sleep(2)
            exit()
            break
        else:
            clrscr()
            print( "Invalid Choice !")
            sleep(2)
main()