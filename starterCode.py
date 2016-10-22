import pymongo
import sys
from pymongo import MongoClient

def enterOneEntry():
    #Todo 1
    print("Not currently implemented")

def findOneEntry():
    #Todo 2
    print("Not currently implemented")

def findAllEntries():
    #Todo 3
    print("Not currently implemented")

def countAllEntries():
    #Todo 4
    print("Not currently implemented")

def deleteOneEntry():
    #Todo 5
    print("Not currently implemented")

def showAllEntries():
    #Todo 6
    print("Not currently implemented")

def entryNotUnderstood():
    print("I don't recognize your input, please reenter your selection")
    print("Press any button to continue")

def findOption(selection):
    try:
        return {"1" : enterOneEntry,"2" : findOneEntry,"3" : findAllEntries, "4" : countAllEntries, "5" : deleteOneEntry, "6" : showAllEntries}[selection]
    except KeyError:
        return entryNotUnderstood

def main(argv):
    while True:
        print('\n')
        print("Welcome to our MongoDB Workshop. Please select an option")
        print ('-'*60)
        print("(1) Enter an entry into our database")
        print("(2) Query our database for an entry")
        print("(3) Query our database for multiple entries")
        print("(4) Query our database for a count of entries")
        print("(5) Remove one entry from our database")
        print("(6) List all entries from our database")
        print ('-'*60)
        selection = input()
        findOption(selection)()
        input()

if __name__ == "__main__":
    client = MongoClient('INSERT NAME HERE')
    db = client.testdatabase
    collection = db.tasks
    main(sys.argv)
