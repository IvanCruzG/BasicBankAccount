import BasicBankAccount as acc
import mysqlConnector as con

#---------------------------------------------------
# make sure you have account.sql, BasicBankAccount.py , driver.py and
# mysqlConnector in the same directory.
# this is a quick a tempt to show case the use of python and mysqlConnector.
# Also this program simulates an online bank account service where the user
# can log in into an existing account or create one if it doesn't exists.
# Once the user's logged in, then he/she can view his/her savings or checkings.
# He or she can also add funds or remove funds from their checking or savings
# account.
#if files are in txt form, convert account.txt to accoutn.sql and the rest of
#the text files convert them to .py files
#---------------------------------------------------

def main():
    #myacc = acc.BasicBankAccount()
    mydb = con.connectTODB()
    #myacc.createAccount()
    running = True

    #main loop that when accessing basic bank account
    while running == True:
        try:
            print('Welcome! Here re your choices: ')
            print('Enter 1 to log into your account')
            print('Enter 2 to create an account')
            print('Enter 3 to exit \n')
            choice1 = input('Please enter your choice: ')

            if (choice1 == '1'):
                print('You are about to log in...')
                print('press 1 to continue or 2 to exit.')
                choice2 = input('Please enter your choice: ')

                if (choice2 == '1'):
                    name = input('Please enter your name: ')
                    pswd = input('Please Enter your password: ')

                    if (con.checkAccount(name, pswd,mydb) == True):
                        info = con.retriveInfoFromDB(name, pswd, mydb)

                        #initiaize my account constructor (id, name, password, email, funds, savings)
                        myacc = acc.BasicBankAccount(info[3], info[0], info[2], info[1], info[5], info[4])

                        choice2a = ''

                        while (choice2a != '7'):
                            print("Welcome {}, what would you like to do?\n".format(info[0]))
                            print("Press 1) to view funds")
                            print("Press 2) to view savings")
                            print("Press 3) to deposit money into checking account")
                            print("Press 4) to withdraw from checking account")
                            print("Press 5) to deposit money into savings account")
                            print("Press 6) to withdraw from savings account")
                            print("Press 7) to log out \n")

                            choice2a = input("please enter your choice: ")

                            if (choice2a == '1'):
                                myacc.displayFunds()

                            elif (choice2a == '2'):
                                myacc.displaySavings()

                            elif (choice2a == '3'):
                                amount = float(input('Please enter the amount you want to deposit into your checkings account: '))
                                myacc.depositIntoCheckings(amount)
                                con.updateFundsInDB(myacc.getId(), myacc.getFunds(), mydb)

                            elif (choice2a == '4'):
                                amount = float(input("Plese enter the amount you would like to withdraw from your checkings account: "))
                                myacc.withdrawFromcheckings(amount)
                                con.updateFundsInDB(myacc.getId(), myacc.getFunds(), mydb)

                            elif (choice2a == '5'):
                                amount = float(input('Please enter the amount you want to deposit into your savings account: '))
                                myacc.depositIntoSavings(amount)
                                con.updateSavingsInDB(myacc.getId(), myacc.getSavings(), mydb)

                            elif (choice2a == '6'):
                                amount = float(input('Please enter the amount you want to withdraw from your savings account: '))
                                myacc.withdrawFromSavings(amount)
                                con.updateSavingsInDB(myacc.getId(), myacc.getSavings(), mydb)

                            elif (choice2a == '7'):
                                print('Thank you for using our service.')
                                print('going back to main menu \n')
                            else:
                                print('please enter a valid command \n')

                    else:
                        print('Account does not exist.')
                        print('Going back to the main menu.\n')

                elif (choice2 == "2"):
                    print('Thank you for using our service!')
                    running = False

                else:
                    print('Going back to the main menu.\n')

            elif (choice1 == '2'):
                print('You are about to create your account...')
                print('press 1 to continue or 2 to exit.')
                choice3 = input('Please enter your choice: ')

                if (choice3 == '1'):
                    myacc = acc.BasicBankAccount()
                    myacc.createAccount()

                    name = myacc.getName()
                    pswd = myacc.getPasswd()

                    if (con.checkAccount(name, pswd, mydb) == True):
                        print("Account Already exists, we are going back to the main menu.")
                    else:
                        #store account info into database
                        con.addAccountToDB(name, pswd, myacc.getEmail(), mydb)
                        myacc.setId(con.retriveIdFromDB(name, pswd, mydb))

                        choice3a = ''

                        while (choice3a != '7'):
                            print("Welcome {}, what would you like to do?\n".format(name))
                            print("Press 1) to view funds")
                            print("Press 2) to view savings")
                            print("Press 3) to deposit money into checking account")
                            print("Press 4) to withdraw from checking account")
                            print("Press 5) to deposit money into savings account")
                            print("Press 6) to withdraw from savings account")
                            print("Press 7) to log out \n")

                            choice3a = input("please enter your choice: ")

                            if (choice3a == '1'):
                                myacc.displayFunds()

                            elif (choice3a == '2'):
                                myacc.displaySavings()

                            elif (choice3a == '3'):
                                amount = float(input('Please enter the amount you want to deposit into your checkings account: '))
                                myacc.depositIntoCheckings(amount)
                                con.updateFundsInDB(myacc.getId(), myacc.getFunds(), mydb)

                            elif (choice3a == '4'):
                                amount = float(input("Plese enter the amount you would like to withdraw from your checkings account: "))
                                myacc.withdrawFromcheckings(amount)
                                con.updateFundsInDB(myacc.getId(), myacc.getFunds(), mydb)

                            elif (choice3a == '5'):
                                amount = float(input('Please enter the amount you want to deposit into your savings account: '))
                                myacc.depositIntoSavings(amount)
                                con.updateSavingsInDB(myacc.getId(), myacc.getSavings(), mydb)

                            elif (choice3a == '6'):
                                amount = float(input('Please enter the amount you want to withdraw from your savings account: '))
                                myacc.withdrawFromSavings(amount)
                                con.updateSavingsInDB(myacc.getId(), myacc.getSavings(), mydb)

                            elif (choice3a == '7'):
                                print('Thank you for using our service.')
                                print('going back to main menu \n')
                            else:
                                print('please enter a valid command \n')

                elif (choice3 == "2"):
                    print('Thank you for using our service!')
                    running = False

                else:
                    print('Going back to the main menu.\n')

            elif (choice1 == '3'):
                print('Thank you for using our service!')
                running = False

            else:
                print('Enter a valid choice!\n')
        except Exception as e:
            print(e)
        finally:
            mydb.close() #close database

    #name = myacc.getName()
    #pswd = myacc.getPasswd()
    #email = myacc.getEmail()





main()
