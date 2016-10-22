import pymongo
import sys
from pymongo import MongoClient

def enterOneEntry():
    title = input("Enter the task title:  ")

    finished = input("Is your task finished? ")
    if finished.lower() == "yes" :
        finished = True
    else:
        finished = False

    importance = input("How important is this task (1-10)")
    entry = {"title": title,
             "done": finished,
             "importance": importance}
    result = collection.insert_one(entry)
    print("Your entry was successfully added!")
    print(result)

def findOneEntry():
    label = input("Enter the field to search in:  ")
    search = input("Enter the value to search for:  ")
    result = collection.find_one({label:search})
    print(result)

def findAllEntries():
    label = input("Enter the field to search in:  ")
    search = input("Enter the value to search for:  ")
    for entry in collection.find({label:search}):
        print(entry)

def countAllEntries():
    label = input("Enter the field to search in:  ")
    search = input("Enter the value to search for:  ")
    result = collection.find({label:search}).count()
    print("There are " + result + "entries matching the search criteria")

def deleteOneEntry():
    label = input("Enter the field to search in:  ")
    search = input("Enter the value to search for:  ")
    result = collection.delete_one({label:search})
    print("Your entry was successfully deleted!")
    print(result)

def showAllEntries():
    if collection.find().count() < 1:
        print("Your collection is empty")
    else:
        for entry in collection.find():
            print(entry)

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
    client = MongoClient('insert database connection name here')
    db = client.testdatabase
    collection = db.tasks
    main(sys.argv)
