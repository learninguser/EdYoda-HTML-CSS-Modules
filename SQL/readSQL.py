import mysql.connector
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dbname", help="Your DB name")
    parser.add_argument("passwd", help="Your DB password")
    args = parser.parse_args()
    dbname = args.dbname
    passwd = args.passwd

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=passwd,
    database=dbname
    )

    mycursor = mydb.cursor()
    path = os.getcwd()
    f = open(path + '/dummy-user-data.txt',encoding = 'utf-8')
    data = f.read()
    f.close()
    data = data.split('\n')

    try:
        for entry in data:
            mycursor.execute(entry)
    
    except:
        mycursor.execute("DROP TABLE User")
        print(f"TABLE User deleted, please re-run the program to make the entries in your {dbname} database")
    
    finally:
        mydb.commit()
        mycursor.close()