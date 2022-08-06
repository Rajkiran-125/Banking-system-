import database as db
from database import MinimumBalanceError

while True:
    print('''\n____welcome to Bank____

1.open a bank account
2.deposit money
3.withdrow money
4.change your name
5.all transaction and closing balance
0.exit

''')
    choice = int(input('Enter your option: '))
    
    if choice == 1:
        acc_no = int(input('Enter account no: '))
        name = input('Enter your name: ')
        dob = input('Enter date of birth: ')
        address = input('Enter your address: ')
        contact = int(input('Enter your contact no.: '))
        balance = int(input('Enter a balance: '))
        try:
            if balance <= 5000:
                raise MinimumBalanceError
            else:
                db.openaccount(acc_no,name,dob,address,contact,balance)
                print(f'**Congratulation**\nYour Account is opened\nYour account number is {acc_no}')
        except:
            print('Your opening balance should be greater than ₹5000')

    elif choice == 2:
        acc_no = int(input('enter your account no: '))
        amt = int(input('enter a amount: '))
        type = 'deposit'
        db.depositmoney(acc_no,amt,type)
        print(f'₹{amt} deposited into Account {acc_no}')
        
    elif choice == 3:
        acc_no = int(input('enter your account no: '))
        amt = int(input('enter a amount: '))
        type = 'withdraw'
        m = db.balance(acc_no)
        try:
            if m[0] - amt <= 5000:
                raise MinimumBalanceError
            else:
                db.withdrawmoney(acc_no,amt,type)
                print(f'₹{amt} withdraw from Account {acc_no}')
        except MinimumBalanceError:
            print('Minimum balance to be maintained ₹5000')
        
    elif choice == 4:
        acc_no = int(input('Enter the account no. whose name to be change: '))  
        column = ''
        newvalue = ''
        newvalue = input('Enter your new name: ')
        column = 'name'
        db.changename(acc_no,column,newvalue)
        print(f'account no.{acc_no} is name updated')

    elif choice == 5:
        acc_no = int(input('Enter your account number: '))
        data = db.transition(acc_no)
        bal = db.balance(acc_no)
        for i in data:
            print(f'\naccount no.{i[0]}\namount: ₹{i[1]}\ntype: {i[2]}\ndate: {i[3]}')
        print(f'\nclosing balance ₹{bal[0]}')

    elif choice == 0:
        print('Thank you :)')
        break

    else:
        print('\nInvalid choice\nTry again..')

        
             





