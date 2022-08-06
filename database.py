import pymysql
 
con = None 
cur = None
def dbconnect():
    global con,cur
    try: 
        con = pymysql.connect(host= 'localhost',
                            database = 'bank',
                            user = 'root',
                            password = '',
                            port = 3307)
        cur = con.cursor()
    except Exception as e:
        print(e)
 
def dbdisconnect():
    con.close()

def openaccount(acc_no,name,dob,address,contact,balance):
    dbconnect()
    query = f"insert into accounts values ({acc_no},'{name}','{dob}','{address}',{contact},{balance})"
    cur.execute(query)
    con.commit()
    dbdisconnect()

def changename(acc_no,column,newvalue):
    dbconnect()
    query = f'update acc set {column} = "{newvalue}" where acc_no = {acc_no}'
    cur.execute(query)
    con.commit()
    dbdisconnect()

def depositmoney(acc_no,amt,type):
    dbconnect()
    query1 = f'update accounts set balance = balance + {amt} where acc_no = {acc_no}'
    cur.execute(query1)
    con.commit()
    query2 = f"insert into trans (acc_no,amt,type) values({acc_no},{amt},'{type}') "
    cur.execute(query2)
    con.commit()
    dbdisconnect()

def balance(acc_no):
    dbconnect()
    query = f'select balance from accounts where acc_no = {acc_no}'
    cur.execute(query)
    record = cur.fetchone()
    dbdisconnect()
    return record

def withdrawmoney(acc_no,amt,type):
    dbconnect()
    query = f'update accounts set balance = balance - {amt} where acc_no = {acc_no}'
    cur.execute(query)
    con.commit()
    query2 = f"insert into trans (acc_no,amt,type) values({acc_no},{amt},'{type}') "
    cur.execute(query2)
    con.commit()
    dbdisconnect()
  
def transition(acc_no):
    dbconnect()
    query = f'select * from trans where acc_no = {acc_no}'
    cur.execute(query)
    record = cur.fetchall()
    dbdisconnect()
    return record

class MinimumBalanceError(Exception):
    pass



   



    
    

    


