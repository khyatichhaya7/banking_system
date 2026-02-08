import mysql.connector
import time as t
    #forsql
amount=int(input("Enter Your Initial Balance"))
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="khyati814",
    database="bank"
    )
cur=con.cursor()
    #debit function with insert in table and print statement
def debit():
    global amount
    debit_amount=int(input("Enter Amount to be Debit"))
    if debit_amount<amount:
        amount=amount-debit_amount
        credit_amount=0
        print("Balance:",amount)
        time_stamp=t.ctime()
        sql="insert into passbook(amount, credit, debit,time) values(%s,%s,%s,%s)"
        values=(amount,credit_amount,debit_amount,time_stamp)
        cur.execute(sql,values)
        con.commit()
        print("Data Inserted Succesfuly into Table")
        print("Thank You for using this Function")
        file=open("statement.txt","a")
        a=(f'  == Amount Debit Succesfully==\n Bank Name     : IMR Bank\n Debit Amount : {debit_amount}\n Balance       : {amount}\n Time          : {time_stamp}\n')
        file.write(a)
        file.write("-"*80+"\n")
    else:
        print("Insufficient Balance")
    #credit function with insert in table and print statement
def credit():
    global amount
    credit_amount=int(input("Enter Amount to be Credit")) 
    amount=amount+credit_amount
    debit_amount=0 
    print("Balance:",amount)
    time_stamp=t.ctime()
    sql="insert into passbook(amount, credit, debit,time) values(%s,%s,%s,%s)"
    values=(amount,credit_amount,debit_amount,time_stamp)
    cur.execute(sql,values)
    con.commit()
    print("Data Inserted Succesfuly into Table")
    print("Thank You for using this Function")
    file=open("statement.txt","a")
    a=(f'  == Amount Credit Succesfully==\n Bank Name     : IMR Bank\n Credit Amount : {credit_amount}\n Balance       : {amount}\n Time          : {time_stamp}\n')
    file.write(a)
    file.write("-"*80+"\n")
def show_balance():
    global amount
    print("Your Balance:",amount) 
    print("Thank You for using this Function")
while True:
    print("========Banking System=========")
    x=int(input(f'Enter Your Choice\n1 : For Debit \n2 : For Credit\n3 : For Show Balance\n4 : For Exit'))
    if x==1:
        debit()
    elif x==2:
        credit()
    elif x==3:
        show_balance()
    elif x==4:
        print("Thank You For Visiting My Banking System")
        break
    else:
        print("Invalid Choice")