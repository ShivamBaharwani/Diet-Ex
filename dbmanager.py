import mysql.connector as connector

class DBHelper:
    def __init__(self):
        # Connect to the database
        self.con = connector.connect(
            host= 'localhost',
            port='3306',
            user= 'root',
            password= '1234',
            database='DietEx')
        
        #queries
        #create table
        query ='CREATE TABLE IF NOT EXISTS userData(userId int, Entry varchar(200), dateTime varchar(200))'
        cur =self.con.cursor()
        cur.execute(query)
        print('Created')
        # print(self.con)

    #insert values
    #creating a method to insert values
    def insert_user(self, userid, entry, dateTime):
        query = "INSERT into userData(userId, entry, dateTime) values({},'{}','{}')".format(userid,entry,dateTime)
        print(query)
        cur =self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('User saved to db')

    #Fech all
    def fech_all(self):
        # query = "SELECT * from userData"
        query = "SELECT users.userId, users.userName, userData.Entry, userData.dateTime FROM userData JOIN users ON userData.userId = users.userId"
        # print(query)
        cur = self.con.cursor()
        cur.execute(query)
        i=1
        for row in cur:
            # print(row) # print in the from of tuple
            print('Details of user',i)
            print('User Id : ',row[0])
            print('Entry : ',row[1])
            print('dateTime : ',row[2])
            print()
            i+=1
        # self.con.commit()
        print('All data feched!')

    #fech perticular user details 
    def fech(self, id):
        # query='SELECT * from userData WHERE userId={}'.format(id)
        query = "SELECT users.userId, users.userName, userData.Entry, userData.dateTime FROM userData JOIN users ON userData.userId = users.userId where users.userId={}".format(id)
        cur=self.con.cursor()
        cur.execute(query)    
        i=1
        for row in cur:
            print('Details of user',i)
            print('User Id : ',row[0])
            print('Entry : ',row[1])
            print('dateTime : ',row[2])
            print()
            i+=1
    
    #delete perticular details
    def delete(self, id):
        query="DELETE from userData where userId ={}".format(id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Data deleted!')

    # Update values
    # def update(self, id,entry, dateTime):
    #     query= "UPDATE user SET entry='{}', dateTime = '{}' WHERE userId = {}".format(entry,dateTime,id)
    #     cur=self.con.cursor()
    #     cur.execute(query)
    #     self.con.commit()
    #     print("values updated!!")


