import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="srajan",
    password="Project@123",
    database="djangodb"
)
cursor=mydb.cursor()
#cursor.execute("create table stud(name varchar(200),age int(50))")

def into():
    name=input()
    age=input()
    line="insert into stud values(%s,%s)"
    val=(name,age)
    cursor.execute(line,val)
#into()
mydb.commit()
cursor.execute("select * from stud")
for x in cursor:
    print('Name: '+x[0]+'\tAge: '+str(x[1]))