import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

coursesObj = open("courses.csv")
coursesDict=csv.DictReader(coursesObj)

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...
q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)    #run SQL query

for i in d:
    c.execute("INSERT INTO students VALUES('"+i["name"]+"',"+ i["id"]+")")

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)

for i in coursesDict:
    c.execute("INSERT INTO courses VALUES('"+i["code"]+"',"+ i["id"]+ ","+i["mark"]+")")

#==========================================================
db.commit() #save changes
db.close()  #close database


