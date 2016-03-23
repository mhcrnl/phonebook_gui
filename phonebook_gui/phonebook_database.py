import sqlite3

# Connect to database 'phonebook.db'
conn = sqlite3.connect('phonebook.db')

def createTable():
    # Create a table named PHONE_BOOK
    conn.execute("CREATE TABLE if not EXISTS PHONE_BOOK ( \
                 ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                 FIRST_NAME TEXT, \
                 LAST_NAME TEXT, \
                 PHONE_NUMBER TEXT, \
                 EMAIL TEXT \
                 );")

def printData(data):
    for row in data:
        print "Id:", row[0]
        print "First Name:", row[1]
        print "Last Name:", row[2]
        print "Phone Number:", row[3]
        print "Email Address:", row[4], "\n"

def newContact(fName,lName,phone,email):
    # Create values part of sql command
    val_str = "'{}', '{}', {}, '{}'".format(\
        fName, lName, phone, email)

    sql_str = "INSERT INTO PHONE_BOOK \
        (FIRST_NAME, LAST_NAME, PHONE_NUMBER, EMAIL) \
        VALUES ({});".format(val_str)
    print sql_str

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def viewAll():
    # Create sql string
    sql_str = "SELECT * from PHONE_BOOK"
    cursor = conn.execute(sql_str)

    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

def updateContact(change_id,fName,lName,phone,email):
    # Create values part of sql command
    val_str = "FIRST_NAME='{}', LAST_NAME='{}',\
              PHONE_NUMBER={}, EMAIL='{}'".format(\
              fName, lName, phone, email)

    sql_str = "UPDATE PHONE_BOOK set \
       {} where ID={};".format(val_str,change_id)
    print sql_str

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def deleteContact(change_id):
    # Create sql string
    sql_str = "DELETE from PHONE_BOOK where ID={}"\
             .format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes


createTable()
