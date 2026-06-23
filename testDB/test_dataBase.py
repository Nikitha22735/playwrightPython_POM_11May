import sqlite3

import pytest

@pytest.mark.db
def test_sqlites_connection():
    dataTables = sqlite3.connect("C:/Users/Nikitha/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db")
    data = dataTables.cursor()
    data.execute('select * from Album')
    # data.execute('''select * from Album 
    #              djgfkjdshfds jkdhfkslkfjdsksl;df 
    #              nlkdjglsjgds;kgdsgds 
    #              nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 
    #              jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj 
    #             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj''')
    # results = data.fetchall()
    # print(len(results))
    # print(data.fetchone())
    # print(data.fetchmany(5))
    # fiveRows = data.fetchmany(5)
    # print(fiveRows[2:4])
    # dataTables.close()

    print(data.description)

# ==============================================MYSQL===================================


# pip install mysql-connector-python
import mysql.connector

def test_mysql_connection():
    dataTables = mysql.connector.connect(host="anyhost", port=3346, database="db", username=os.getenv("user"), password="pw")
    data = dataTables.cursor()
    data.execute('select * from Album')
    # data.execute('''select * from Album 
    #              djgfkjdshfds jkdhfkslkfjdsksl;df 
    #              nlkdjglsjgds;kgdsgds 
    #              nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 
    #              jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj 
    #             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj''')
    # results = data.fetchall()
    # print(len(results))
    # print(data.fetchone())
    # print(data.fetchmany(5))
    # fiveRows = data.fetchmany(5)
    # print(fiveRows[2:4])
    # dataTables.close()

    print(data.description)


# ==============================================Oracle===================================
# pip install oracledb
import oracledb

def test_oracle_connection():
    dataTables = oracledb.connect(username=os.getenv("user"), password="pw", role="qa")
    data = dataTables.cursor()
    data.execute('select * from Album')
    # data.execute('''select * from Album 
    #              djgfkjdshfds jkdhfkslkfjdsksl;df 
    #              nlkdjglsjgds;kgdsgds 
    #              nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 
    #              jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj 
    #             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj''')
    # results = data.fetchall()
    # print(len(results))
    # print(data.fetchone())
    # print(data.fetchmany(5))
    # fiveRows = data.fetchmany(5)
    # print(fiveRows[2:4])
    # dataTables.close()

    print(data.description)


# ==============================================postgress===================================
# pip install psycopg2-binary
import psycopg2
def test_mysql_connection():
    dataTables = psycopg2.connect(host="anyhost", port=3346, database="db", username=os.getenv("user"), password="pw")
    data = dataTables.cursor()
    data.execute('select * from Album')
    # data.execute('''select * from Album 
    #              djgfkjdshfds jkdhfkslkfjdsksl;df 
    #              nlkdjglsjgds;kgdsgds 
    #              nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn 
    #              jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj 
    #             jjjjjjjjjjjjjjjjjjjjjjjjjjjjjj''')
    # results = data.fetchall()
    # print(len(results))
    # print(data.fetchone())
    # print(data.fetchmany(5))
    # fiveRows = data.fetchmany(5)
    # print(fiveRows[2:4])
    # dataTables.close()

    print(data.description)