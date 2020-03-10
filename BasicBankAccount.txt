class BasicBankAccount:

    #----------------------------------------------------------------------
    # This file contains code that instantiates and account and alters it.
    #----------------------------------------------------------------------

    #create a constructor for user that contains their information.
    def __init__(self, id=0, name='', pswd='', email = '', funds = 0, savings = 0):
        self.__id = id
        self.__name = name
        self.__pswd = pswd
        self.__email = email
        self.__funds = funds
        self.__savings = savings

    #define setters
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setPasswd(self, pswd):
        self.pswd = pswd

    def setEmail(self, email):
        self.__email = email

    def setFunds(self, funds):
        self.__funds = funds

    def setSavings(self, savings):
        self.__savings = savings

    #define getters
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPasswd(self):
        return self.__pswd

    def getEmail(self):
        return self.__email

    def getFunds(self):
        return self.__funds

    def getSavings(self):
        return self.__savings

    def createAccount(self):
        choice = 'n'

        while (choice != 'y'):
            print('Here are your choices:')
            print('Press 1) to enter your name')
            print('Press 2) to enter your password')
            print('Press 3) to enter your email')
            print('Press y) to submit')
            print('Make sure you have entered at least your name and password before continuing')
            print("\n")
            choice = input('Enter your choice: ')

            if (choice == '1'):
                self.__name = input('Enter your name: ')
            elif (choice == '2'):
                self.__pswd = input('Create password: ')
            elif (choice == '3'):
                self.__email = input('Enter your email address: ')
            elif (choice == 'y'):
                if ( not(self.__name and self.__name.strip()) or not(self.__pswd and self.__pswd.strip()) ):
                    choice = 'n'
                else:
                    choice = 'y'
            else:
                print('Please enter a valid command \n')

    def depositIntoCheckings(self, amount):
        try:
            if (amount > 0):
                self.__funds += amount
            else:
                print('going back to the menu')
        except ValueError:
            print('you did not enter a proper value.')

    def depositIntoSavings(self, amount):
        try:
            if (amount > 0):
                self.__savings += amount
            else:
                print('going back to the menu')
        except ValueError:
            print('You did not enter a proper value.')

    def withdrawFromcheckings(self, amount):
        try:
            if (amount > 0 and self.__funds - amount >= 0):
                self.__funds -= amount
            elif (amount > self.__funds):
                print('You do not have enough funds.')
        except ValueError:
            print('enter a correct amount')

    def withdrawFromSavings(self, amount):
        try:
            if (amount > 0 and self.__savings - amount >= 0):
                self.__savings -= amount

            elif (amount > self.__savings):
                print('not enough funds in savings account.')
        except ValueError:
            print('enter a correct amount')

    def displayFunds(self):
        print(self.__funds)

    def displaySavings(self):
        print(self.__savings)


if __name__ == '__main__':
    print('hello world!')
    myacc = BasicBankAccount()
    #myacc.setName('ivan')
    #print(myacc.getName())
    #mydb = con.connectTODB();
    #print(con.getLengthOfDB(mydb))
    myacc.createAccount()
    myacc.depositIntoCheckings(35)
    print(myacc.getFunds())
