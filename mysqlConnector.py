import mysql.connector

#----------------------------------------
# This file access account table and updates it
#----------------------------------------

def connectTODB():
    return mysql.connector.connect(
        user="root",
        password="Sangria2",
        database="bankaccount"
    )
#using account table

def getLengthOfDB(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM account")
    return len(mycursor.fetchall())

def displayTables(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for tb in mycursor:
        print(tb)

def addAccountToDB(name, pswd, email, mydb):
    arg = """INSERT INTO account (name, password, email, funds, savings) VALUES
    (%s,%s,%s,%s,%s)"""
    values = (name, pswd, email, "0", "0")
    mycursor = mydb.cursor()
    mycursor.execute(arg,values)
    mydb.commit()
    print(mycursor.rowcount, "account created.")

def retriveIdFromDB(name, pswd, mydb):
    mycursor = mydb.cursor()
    arg = "SELECT id FROM account WHERE name = '{}' AND password = '{}'".format(name,pswd)
    mycursor.execute(arg)
    return mycursor.fetchone()[0] #return id

def retriveFundsFromDB(id, mydb):
    mycursor = mydb.cursor()
    arg = "SELECT funds FROM account WHERE id = {}".format(id)
    mycursor.execute(arg)
    return mycursor.fetchone()[0]


def retriveSavingsFromDB(id, mydb):
    mycursor = mydb.cursor()
    arg = "SELECT savings FROM account WHERE id = {}".format(id)
    mycursor.execute(arg)
    return mycursor.fetchone()[0]

def updateFundsInDB(id,funds,mydb):
    mycursor = mydb.cursor()
    arg = "UPDATE account SET funds = {} WHERE id = {}".format(funds,id)
    mycursor.execute(arg)
    mydb.commit()

def updateSavingsInDB(id,savings,mydb):
    mycursor = mydb.cursor()
    arg = "UPDATE account SET savings = {} WHERE id = {}".format(savings,id)
    mycursor.execute(arg)
    mydb.commit()

def checkAccount(name, pswd, mydb):
    mycursor = mydb.cursor()
    arg = "SELECT * FROM account"
    mycursor.execute(arg)
    myresult = mycursor.fetchall()

    #check if name and password are in the database
    for acc in myresult:
        if (name in acc and pswd in acc):
            print(acc)
            return True
        else:
            return False

def retriveInfoFromDB(name, pswd, mydb):
    mycursor = mydb.cursor()
    arg = "SELECT * FROM account"
    mycursor.execute(arg)
    return  mycursor.fetchone()

#mydb.close()
if __name__ == "__main__":
    print('hello')
    mydb = connectTODB()

    checkAccount('ivan', 'sand', mydb)
