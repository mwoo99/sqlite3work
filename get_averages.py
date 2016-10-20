import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()
d = db.cursor()

def getAverage(studentID):
    gradeSum = 0;
    gradeCounter = 1;
    query = "SELECT mark FROM courses WHERE courses.id = " + str(studentID) + ";"
    grades = c.execute(query)
    for record in grades:
        gradeSum+=record[0]
        gradeCounter+=1
    return float(gradeSum)/gradeCounter

def printAvgs():
    query = "SELECT name, id FROM students"
    avgData = d.execute(query)
    for record in avgData:
        print "Name: %s , Id: %d , Average: %f" %(record[0], record[1], getAverage(record[1]))

printAvgs()

db.commit()
db.close()
