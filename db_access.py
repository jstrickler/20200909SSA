import sqlite3   # module for sqlite3
import psycopg2  # module for Postgres
import pymysql   # module for MySQL

#  cx_oracle pymysql pymssql pyodbc ...

sqlite_conn = sqlite3.connect('DATA/presidents.db')
postgres_conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='scripts')
mysql_conn = pymysql.connect(host='localhost', db='presidents', user='scripts', password='scripts')

for conn in sqlite_conn, postgres_conn, mysql_conn:

    cursor = conn.cursor()

    cursor.execute("""select firstname, lastname from presidents where party = 'Whig'""")

    for row in cursor.fetchall():
        print(row)

    print('-' * 60)

sqlite_conn.close()
postgres_conn.close()
mysql_conn.close()
