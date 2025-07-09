import sqlite3
from employee import Employee


# DAL module

def connectDB():
    ''' Connects to sqlite3 database called emp.db'''
    global conn
    conn = sqlite3.connect('emp.db')
    global cursor
    cursor = conn.cursor()
    print("Connected to Emp. db")


# ---------------------------------------------------
def create_table():
    '''create emp table '''
    try:
        cmd = "CREATE TABLE emps(first text, last text, pay integer)"
        cursor.execute(cmd)
        print("Emps table is created")
    except Exception as ex:
        print(ex)


# ---------------------------------------------------

def insertEmp(emp):
    try:
        cmd = "INSERT INTO emps(first,last,pay) VALUES (?,?,?)"
        values = (emp.first, emp.last, emp.pay)
        cursor.execute(cmd, values)
        cursor.execute('commit')
        print("One record inserted")
    except  Exception as ex:
        print('can not insert', ex)


# --------------------------------------------------------
def getEmps():
    cursor.execute("SELECT * FROM emps")
    return cursor.fetchall()


# --------------------------------------------------------
def removeEmp(emp):
    cursor.execute("DELETE FROM emps WHERE :last=last", {'last': emp.last})
    cursor.execute('commit')
    print("one record deleted")


# ---------------------------------------------------------
if __name__ == '__main__':
    print("Testing database API")
    connectDB()
    # create_table()
    '''
    emp1=Employee("Sriram","Murthy",50000)
    emp2=Employee("Raj",'Kumar',60000)
    insertEmp(emp1)
    insertEmp(emp2)
    '''
    emps = getEmps()
    print(emps)  # [ (),()]

    emp = Employee("Raj", 'Kumar', 60000)
    removeEmp(emp)
    print("After removing records")
    emps = getEmps()
    print(emps)  # [ (),()]

    conn.close()
    print("All work done")


