#accountNo = 0
#cusName = ' '
#Branchco = ' '
#Mobile = 0
#Balance = 0
#widthdraw = ' '
def createaccounts():
    accountNo = int(input('Enter account number'))
    cusName = input('Enter name')
    Branchco = input('Enter code')
    Mobile = int(input('Enter mobile number'))
    balance = int(input('enter balance'))
    widthdraw = input('Enter widthdraw')

#def showAcntDetails():
 #   print('Accountno:',accountNo)
  #  print('Customer name:',cusName)
   # print('Branch code:',Branchco)
    #print('Mobile:',Mobile)
    #print('Balance:',Balance)
    #print('widthdraw:',widthdraw)

#def Deposit(amount):
 #   balance = Balance + amount
  #  checkBalance()


#def widthdraw(amount):
 #   widthdraw = Balance - amount
  #  checkBalance()

#def checkBalance():
 #   print('current Balance:',Balance)

print('1.Create account\n 2.Widthdraw\n 3.Deposit\n 4.checkBalance')
ch=int(input('select any option'))
if(ch==1):
    createaccounts()
elif(ch==2):
    amount = int(input('Enter the Widthdraw:'))
    #widthdraw(amount)
elif(ch==3):
    amount = int(input('Enter The Deposit:'))
   # Deposit(amount)
#elif(ch==4):
    #checkBalance()
else:
    print('Select any 4 options available:')




