# pip install mysql-connector-python
import mysql.connector as mySQL

def Cursor(h,u,p,db=None):
    # DATABASEselected = input("Enter the database name: ")
    DB = mySQL.connect(
        host=h,
        user=u,
        password=p,
        database=db
    )
    
    return DB.cursor(), DB
